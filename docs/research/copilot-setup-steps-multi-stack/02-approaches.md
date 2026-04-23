# 02 — Approaches to Dynamic `copilot-setup-steps.yml`

> Each approach is rated on: **Setup Time Saved** · **Complexity** · **Feasibility Today**

---

## Approach 1 — File/Path-Based Detection with `if:` Guards

### How it works

Inspect the repository for stack-indicator files (`pom.xml`, `package.json`, `requirements.txt`, `Podfile`, etc.) at the start of the setup job, store the result in an environment variable or step output, and gate subsequent steps behind `if:` conditions.

```yaml
jobs:
  copilot-setup-steps:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Detect stacks
        id: detect
        run: |
          echo "java=$(test -f pom.xml && echo true || echo false)" >> $GITHUB_OUTPUT
          echo "node=$(test -f package.json && echo true || echo false)" >> $GITHUB_OUTPUT
          echo "python=$(test -f requirements.txt && echo true || echo false)" >> $GITHUB_OUTPUT

      - name: Set up Java
        if: steps.detect.outputs.java == 'true'
        uses: actions/setup-java@v4
        with:
          java-version: '21'
          distribution: 'temurin'

      - name: Set up Node.js
        if: steps.detect.outputs.node == 'true'
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - name: Set up Python
        if: steps.detect.outputs.python == 'true'
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
          cache: 'pip'
```

### Pros

- Works today with zero GitHub-specific features
- File presence is a reliable, durable signal
- Easy to read and maintain
- Reduces setup time proportionally to how many stacks are absent
- `if:` conditions are fully supported in `copilot-setup-steps`

### Cons

- Only detects **what exists in the repo**, not **what the specific task touches**
- Monorepos with all stacks present install everything every run
- Requires a checkout step before detection (adds ~10-15 sec)
- Cannot distinguish between a Java task and a frontend task in a full-stack repo

### Feasibility verdict

✅ **Fully supported today.** This is the most practical near-term approach for repos where stacks are clearly separated into different subdirectories. Works even better with path-scoped detection:

```bash
echo "java=$(test -f backend/pom.xml && echo true || echo false)" >> $GITHUB_OUTPUT
```

**Sources**: [GitHub Actions `if` conditions](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/evaluate-expressions-in-workflows-and-actions) · [actions/setup-java](https://github.com/actions/setup-java)

---

## Approach 2 — Environment Variables and Repository Variables

### How it works

Use [GitHub Actions variables](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/store-information-in-variables) (repository-level or environment-level) to declare the "active stack", then read them in setup steps.

```yaml
      - name: Set up Java (if ACTIVE_STACK includes java)
        if: contains(vars.ACTIVE_STACKS, 'java')
        uses: actions/setup-java@v4
        with:
          java-version: '21'
          distribution: 'temurin'
```

Repository variables can be set via the GitHub UI or API: **Settings → Secrets and variables → Variables**.

### Pros

- No checkout required to read `vars.*`
- Can be changed without a code commit (UI/API update)
- Works for stable, long-running stack configurations
- `ACTIVE_STACKS` could be a comma-separated list: `"java,python"`

### Cons

- Variables are **repo-wide or environment-wide** — cannot be set per-issue or per-PR without external tooling
- Requires manual maintenance (someone must update the variable when the active stack changes)
- Not dynamic per Copilot session

### Feasibility verdict

⚠️ **Partial.** Useful as a coarse-grained toggle ("this repo only uses Java right now") but cannot adapt per-task. Combine with Approach 1 for better results.

**Sources**: [Storing information in variables](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/store-information-in-variables)

---

## Approach 3 — Issue/PR Labels as Stack Selectors

### How it works

Apply labels such as `stack:java`, `stack:frontend` to issues/PRs, then read the event payload in the setup job to enable only the matching stacks.

```yaml
      - name: Parse stack labels
        id: labels
        run: |
          LABELS='${{ toJson(github.event.issue.labels.*.name) }}'
          echo "java=$(echo $LABELS | grep -c 'stack:java' | grep -q 1 && echo true || echo false)" >> $GITHUB_OUTPUT
```

### Pros

- Per-issue/PR granularity — the finest level of control possible
- Labels are cheap to apply and remove
- Self-documenting: labels are visible in the UI

### Cons

- Requires understanding of whether `github.event` is populated during setup — see `03-event-payload-access.md` for the full analysis (answer: **uncertain/unreliable**)
- Someone must apply labels before the Copilot session starts
- Fragile if labels are forgotten or mis-spelled
- JSON parsing in bash is error-prone without `jq`

### Feasibility verdict

⚠️ **Uncertain today.** The critical blocker is event payload access (see `03-event-payload-access.md`). If GitHub confirms event context is available, this approach becomes very powerful. Until then, treat as experimental.

---

## Approach 4 — Composite Actions per Stack

### How it works

Extract each stack's setup into a [composite action](https://docs.github.com/en/actions/sharing-automations/creating-actions/creating-a-composite-action) stored in `.github/actions/`:

```
.github/actions/
├── setup-java-backend/action.yml
├── setup-frontend/action.yml
└── setup-python-ml/action.yml
```

Call them conditionally:

```yaml
      - name: Set up Java backend
        if: steps.detect.outputs.java == 'true'
        uses: ./.github/actions/setup-java-backend
```

Each `action.yml` encapsulates all steps for that stack (SDK install, dependency cache, tool installs).

### Pros

- Clean separation of concerns — each stack owns its setup
- Composite actions are reusable across repositories (if published)
- Easier to review and test changes to one stack in isolation
- Secrets and environment variables are fully accessible inside composite actions

### Cons

- Does **not** reduce total setup time on its own — it's a code organization tool
- Still requires a checkout before the composite action can be referenced (local path)
- Adds one level of indirection that may confuse new contributors

### Feasibility verdict

✅ **Fully supported today.** Best used in combination with Approaches 1 or 3 for conditional execution. This is a **maintenance win**, not a performance win.

**Sources**: [Creating a composite action](https://docs.github.com/en/actions/sharing-automations/creating-actions/creating-a-composite-action)

---

## Approach 5 — The `snapshot` Feature (Environment Caching)

### How it works

The `snapshot: true` setting tells Copilot to capture the runner environment after setup and reuse it for subsequent sessions, bypassing re-installation.

```yaml
jobs:
  copilot-setup-steps:
    runs-on: ubuntu-latest
    snapshot: true
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v4
        with:
          java-version: '21'
          distribution: 'temurin'
```

See `04-snapshot-deep-dive.md` for full analysis.

### Pros

- Near-zero setup time for cached sessions
- No code changes needed beyond adding `snapshot: true`
- Works transparently — agent sees the same environment

### Cons

- Snapshot covers **all stacks** — no per-stack granularity
- Cache invalidation is opaque (unclear what triggers a rebuild)
- If the snapshot is stale, the agent may have outdated dependencies
- Not yet GA — availability and behavior may change

### Feasibility verdict

⚠️ **Available in preview.** The biggest win for pure setup speed, but all-or-nothing. Best for stable environments where all stacks are needed regardless.

**Sources**: [Customizing the development environment](https://docs.github.com/en/copilot/customizing-copilot/customizing-the-development-environment-for-copilot-coding-agent)

---

## Approach 6 — `services` Containers

### How it works

Use the `services` key to run sidecar containers (databases, message brokers, mock servers) instead of installing them in steps:

```yaml
jobs:
  copilot-setup-steps:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:16
        env:
          POSTGRES_PASSWORD: postgres
        ports:
          - 5432:5432
      redis:
        image: redis:7
        ports:
          - 6379:6379
    steps:
      - uses: actions/checkout@v4
      # No need to install/start postgres or redis in steps
```

### Pros

- Services start in parallel with step execution (minor time saving)
- Cleaner than installing services via `apt` in steps
- Standard Docker networking — services are accessible via `localhost:<port>`
- No maintenance of service installation scripts

### Cons

- Applies to **all sessions** — cannot conditionally start a service
- Adds Docker pull time if images aren't cached
- Memory/CPU overhead for running containers alongside agent
- Does not help with SDK installs (Java, Node, Python toolchains)

### Feasibility verdict

✅ **Fully supported today.** Best used to offload infrastructure services (DBs, caches, queues) out of serial steps. Does not address the core multi-stack SDK problem.

**Sources**: [About service containers](https://docs.github.com/en/actions/use-cases-and-examples/service-containers/about-service-containers)

---

## Approach 7 — Larger Runners

### How it works

Switch from `ubuntu-latest` (2-core) to a larger runner:

```yaml
jobs:
  copilot-setup-steps:
    runs-on: ubuntu-22.04-4-core
```

### Pros

- Faster I/O, faster compilation, faster npm/pip installs
- No code changes to individual steps
- Can meaningfully reduce wall-clock setup time for CPU/IO-bound installs

### Cons

- Costs more per minute (~2-4× depending on size)
- Does **not** change the serial execution model
- Diminishing returns — most installs are network-bound, not CPU-bound
- Estimated savings: 20-40% for heavy installs, less for download-heavy steps

### Feasibility verdict

✅ **Fully supported today.** A simple, low-risk optimization. Combine with other approaches for maximum benefit.

**Sources**: [About larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/about-larger-runners)

---

## Approach 8 — Separate Repositories per Stack

### How it works

Split the monorepo into per-stack repositories, each with its own minimal `copilot-setup-steps.yml`:

```
my-org/backend-java    → copilot-setup-steps: Java only
my-org/frontend-react  → copilot-setup-steps: Node only
my-org/ml-python       → copilot-setup-steps: Python only
```

### Pros

- Each repo has minimal, targeted setup — maximum speed
- No conditional logic needed
- Clear ownership boundaries
- Copilot can be scoped to the relevant repo per-task

### Cons

- Fundamentally changes the repository architecture
- Cross-cutting changes (shared libs, contracts, migrations) span multiple PRs
- Code sharing requires packages/submodules — significant overhead
- Not practical for existing monorepos without major refactoring

### Feasibility verdict

✅ **Technically feasible** but only as an architectural decision, not a tactical fix. Not recommended unless the monorepo split was already planned.

---

## Approach 9 — Copilot Instructions as a Runtime Workaround

### How it works

Add instructions to `.github/copilot-instructions.md` telling the agent to self-install missing dependencies at the start of its session:

```markdown
## Setup Instructions

If you need to run Java code and `java` is not available:
  run: sdk install java 21.0.3-tem

If you need to run Node.js and `node` is not available:
  run: nvm install 20 && nvm use 20
```

### Pros

- No changes to `copilot-setup-steps.yml`
- Agent can dynamically detect and install only what it needs
- Zero setup time for stacks not required

### Cons

- **Reliability**: Agent may not always follow instructions precisely
- **Speed**: Agent burns task time on setup instead of coding
- **Security**: Giving the agent broad install permissions increases attack surface
- **Consistency**: Environment may vary between sessions
- Not a substitute for a proper pre-built environment

### Feasibility verdict

⚠️ **Possible but not recommended** as a primary strategy. Useful as a fallback for occasional one-off dependencies.

---

## Approach 10 — Custom Self-Hosted Runner Images

### How it works

Pre-bake all SDK tooling into a custom Docker image or VM image used as a self-hosted runner:

```yaml
jobs:
  copilot-setup-steps:
    runs-on: self-hosted   # Uses your custom image
    steps:
      - uses: actions/checkout@v4
      # All SDKs already installed — steps are just dependency installs
      - run: mvn dependency:go-offline   # Fast: JDK already present
      - run: npm ci                       # Fast: Node already present
```

### Pros

- Dramatically reduces setup time — SDKs present from image start
- Full control over environment composition
- Can create per-stack images and route with `runs-on` labels
- Snapshot-equivalent without needing the GitHub-managed snapshot feature

### Cons

- Requires self-hosted runner infrastructure (maintenance, security, cost)
- Image must be kept current (patching, SDK updates)
- Self-hosted runners have security implications for public repos
- GitHub's Copilot orchestrator compatibility with self-hosted runners should be verified

### Feasibility verdict

✅ **Fully supported** if self-hosted runner infrastructure exists. The most powerful approach for organizations already running self-hosted runners. High upfront cost, maximum long-term benefit.

**Sources**: [About self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/about-self-hosted-runners)

---

## Comparison Matrix

| Approach | Setup Time Saved | Complexity | Cost Impact | Feasible Today? |
|---|---|---|---|---|
| 1. File detection + `if:` | Medium | Low | None | ✅ Yes |
| 2. Repository variables | Low | Low | None | ✅ Yes |
| 3. Issue/PR labels | High (if works) | Medium | None | ⚠️ Uncertain |
| 4. Composite actions | None (org only) | Medium | None | ✅ Yes |
| 5. Snapshot caching | Very High | Low | None | ⚠️ Preview |
| 6. Services containers | Low | Low | Minor | ✅ Yes |
| 7. Larger runners | Medium | Very Low | 2-4× | ✅ Yes |
| 8. Separate repos | Very High | Very High | None | ✅ Yes |
| 9. Copilot instructions | Medium | Low | None | ⚠️ Unreliable |
| 10. Custom runner images | Very High | High | Infrastructure | ✅ Yes |
