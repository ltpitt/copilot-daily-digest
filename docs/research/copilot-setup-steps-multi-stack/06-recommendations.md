# 06 — Ranked Recommendations

> Actionable guidance for a lead developer to pick the right approach for their multi-stack repo.

---

## Recommendation 1 (Do This Now): File-Based Detection + `if:` Guards

**Effort**: Low (1-2 hours) · **Impact**: Medium-High · **Risk**: Low

Add a detect-stacks step at the top of `copilot-setup-steps.yml` and gate every SDK install behind `if:` conditions. This is the highest-value change with the lowest risk.

```yaml
jobs:
  copilot-setup-steps:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Detect active stacks
        id: stacks
        run: |
          echo "java=$(test -f backend/pom.xml && echo true || echo false)" >> $GITHUB_OUTPUT
          echo "node=$(test -f frontend/package.json && echo true || echo false)" >> $GITHUB_OUTPUT
          echo "python=$(test -f ml/requirements.txt && echo true || echo false)" >> $GITHUB_OUTPUT
          echo "swift=$(test -f ios/Podfile && echo true || echo false)" >> $GITHUB_OUTPUT

      - name: Set up Java
        if: steps.stacks.outputs.java == 'true'
        uses: actions/setup-java@v4
        with:
          java-version: '21'
          distribution: 'temurin'

      - name: Set up Node.js
        if: steps.stacks.outputs.node == 'true'
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - name: Set up Python
        if: steps.stacks.outputs.python == 'true'
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
          cache: 'pip'
```

**When this falls short**: In true monorepos where all stack indicator files always exist, this approach cannot distinguish "Java task" from "Frontend task" without richer signals. Move to Recommendation 2.

---

## Recommendation 2 (Do This Next): Add Dependency Caching

**Effort**: Low (30 min) · **Impact**: High · **Risk**: Very Low

After adding `if:` guards, layer in `actions/cache` for each detected stack. This reduces setup time by 60-80% for dependency downloads even on cold (non-snapshot) runs.

```yaml
      - name: Cache Maven repository
        if: steps.stacks.outputs.java == 'true'
        uses: actions/cache@v4
        with:
          path: ~/.m2/repository
          key: ${{ runner.os }}-maven-${{ hashFiles('**/pom.xml') }}
          restore-keys: ${{ runner.os }}-maven-

      - name: Cache npm
        if: steps.stacks.outputs.node == 'true'
        uses: actions/cache@v4
        with:
          path: ~/.npm
          key: ${{ runner.os }}-npm-${{ hashFiles('**/package-lock.json') }}
          restore-keys: ${{ runner.os }}-npm-

      - name: Cache pip
        if: steps.stacks.outputs.python == 'true'
        uses: actions/cache@v4
        with:
          path: ~/.cache/pip
          key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements*.txt') }}
          restore-keys: ${{ runner.os }}-pip-
```

---

## Recommendation 3 (Do This for Organization): Composite Actions per Stack

**Effort**: Medium (half day) · **Impact**: Maintenance quality · **Risk**: Low

Extract each stack's steps (SDK install + cache + dependency install) into a composite action. This does not reduce execution time but makes the workflow vastly more maintainable and reviewable.

```
.github/actions/
├── setup-java-backend/action.yml
├── setup-frontend/action.yml
├── setup-python-ml/action.yml
└── setup-ios/action.yml
```

In the main workflow:
```yaml
      - name: Setup Java backend
        if: steps.stacks.outputs.java == 'true'
        uses: ./.github/actions/setup-java-backend

      - name: Setup frontend
        if: steps.stacks.outputs.node == 'true'
        uses: ./.github/actions/setup-frontend
```

Stack owners can modify their own composite action without touching the main workflow file.

---

## Recommendation 4 (Enable When Available): Snapshot Caching

**Effort**: Trivial (add one line) · **Impact**: Very High · **Risk**: Low-Medium

Once you have completed Recommendations 1-3, enable `snapshot: true`. The snapshot captures the fully-installed environment and near-eliminates setup time for subsequent sessions.

```yaml
jobs:
  copilot-setup-steps:
    runs-on: ubuntu-latest
    snapshot: true          # ← Add this
```

**Precautions**:
- Test snapshot behavior — ensure cache invalidation works when dependencies change
- Monitor for stale dependency issues (outdated packages in snapshot)
- Keep your stack detection and `if:` guards even with snapshot enabled, so the snapshot represents an efficient baseline

---

## Recommendation 5 (For Heavy Infrastructure): Services Containers

**Effort**: Low · **Impact**: Medium · **Risk**: Low

Move database, cache, and message broker setup from steps to `services:`. This reduces step complexity and allows services to start while other steps run.

```yaml
jobs:
  copilot-setup-steps:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:16
        env:
          POSTGRES_PASSWORD: test
        ports:
          - 5432:5432
      redis:
        image: redis:7-alpine
        ports:
          - 6379:6379
```

---

## Recommendation 6 (If Budget Allows): Upgrade to Larger Runners

**Effort**: Trivial · **Impact**: Low-Medium · **Risk**: Low

For heavy multi-stack setups (Java + Node + Python + Docker), a 4-core runner cuts wall-clock setup time by 25-40% and reduces the chance of hitting the 59-minute timeout.

```yaml
    runs-on: ubuntu-22.04-4-core
```

This is purely a cost-speed tradeoff. Combine with other recommendations for compounding benefit.

---

## Do Not Pursue (Yet)

| Approach | Reason to Skip |
|---|---|
| **Label-based routing** | Event payload access is unconfirmed. Revisit when GitHub documents this. |
| **Separate repos per stack** | Architectural change, not a tactical fix. Only valid if repo split was already planned. |
| **Copilot instructions self-install** | Too unreliable for production workflows. Use as last-resort fallback only. |
| **Custom self-hosted runners** | High maintenance cost. Only viable if self-hosted infrastructure already exists. |

---

## Prioritized Decision Table

Use this to pick the right approach in under 5 minutes:

| My Situation | First Action |
|---|---|
| Simple repo (1-2 stacks, some steps always run) | Add `actions/cache` (Rec. 2) + `snapshot: true` (Rec. 4) |
| Monorepo with 3+ stacks, not all needed per task | Add file detection + `if:` guards (Rec. 1) + caching (Rec. 2) |
| Monorepo, maintenance is main concern | Add composite actions (Rec. 3) + detection (Rec. 1) |
| All stacks always needed, just need speed | Enable `snapshot: true` (Rec. 4) + larger runner (Rec. 6) |
| Setup hitting 59-min timeout | Priority: Rec. 1 (reduce what runs) + Rec. 6 (faster hardware) |
| Heavy database/service dependencies | Move to `services:` (Rec. 5) + file detection (Rec. 1) |

---

## Implementation Sequence

For a team starting from scratch on a multi-stack monorepo:

```
Week 1:  Add file detection + if: guards (Rec. 1)
         → Measure: setup time drops for pure-frontend or pure-backend tasks

Week 1:  Add actions/cache for each stack (Rec. 2)
         → Measure: dependency install time drops 60-80%

Week 2:  Refactor into composite actions (Rec. 3)
         → Benefit: stack owners can maintain their own setup

Week 3:  Enable snapshot: true (Rec. 4)
         → Measure: setup time approaches near-zero for cached sessions

Ongoing: Monitor the Copilot changelog for event payload access
         → If confirmed: add label-based routing for finer granularity
```

---

## Roadmap Items to Monitor

| Feature | Why It Matters | Where to Watch |
|---|---|---|
| Event payload in setup steps | Unlocks per-issue/PR stack routing | [Copilot changelog](https://github.blog/changelog/label/copilot/) |
| Per-stack snapshots | Snapshot only the needed stack | GitHub roadmap / changelog |
| Parallel setup jobs | Run stack setups concurrently | GitHub Actions roadmap |

**Sources**: All official sources cited throughout `01-constraints.md`, `02-approaches.md`, `03-event-payload-access.md`, `04-snapshot-deep-dive.md`, and `05-real-world-examples.md`.
