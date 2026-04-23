# 04 — Snapshot Feature Deep Dive

> **Source**: [Customizing the development environment for Copilot coding agent](https://docs.github.com/en/copilot/customizing-copilot/customizing-the-development-environment-for-copilot-coding-agent)

---

## What is the `snapshot` Feature?

The `snapshot` key in `copilot-setup-steps.yml` instructs GitHub to capture the entire runner environment after setup completes and store it as a reusable image. Subsequent Copilot sessions restore from that snapshot instead of re-running all setup steps.

```yaml
jobs:
  copilot-setup-steps:
    runs-on: ubuntu-latest
    snapshot: true          # ← Enable environment caching
    timeout-minutes: 59
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v4
        with:
          java-version: '21'
          distribution: 'temurin'
      - run: mvn dependency:go-offline -f backend/pom.xml
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: npm ci --prefix frontend
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install -r requirements.txt
```

---

## How Snapshotting Works (Inferred)

Based on available documentation and comparable GitHub Actions caching mechanisms:

1. **First run**: Setup steps execute normally. At the end of the job, GitHub captures the environment (installed tools, file system state, environment variables).
2. **Subsequent runs**: The snapshot is restored as the starting environment. Setup steps are skipped (or run in validation mode).
3. **Invalidation**: The snapshot is rebuilt when the `copilot-setup-steps.yml` file changes (inferred — not explicitly documented).

---

## Key Questions and Current Answers

### Q1: What exactly is captured?

| Component | Captured? | Notes |
|---|---|---|
| Installed OS packages (`apt`) | ✅ Yes (inferred) | File system state |
| SDK installations (Java, Node, Python) | ✅ Yes (inferred) | Installed to known paths |
| Maven/npm/pip dependency caches | ✅ Yes (inferred) | `.m2`, `node_modules`, etc. |
| Environment variables | ⚠️ Unknown | May only be set fresh each run |
| GitHub Actions tool cache | ⚠️ Unknown | May be separate from snapshot |
| Repository checkout | ❌ No | Code changes every session |

### Q2: Can you snapshot per-stack?

**No.** There is only one `snapshot: true` field, and it captures the entire environment after all steps complete. There is no mechanism to create multiple named snapshots or select a snapshot per-session.

**Implication**: For a multi-stack repo, you must snapshot ALL stacks together. This is only useful if total setup time (cached) is still less than the raw setup time.

### Q3: How is cache invalidation handled?

Documentation does not specify. Likely triggers:
- Change to `copilot-setup-steps.yml` (most probable)
- Change to dependency files (`pom.xml`, `package.json`, `requirements.txt`)
- Time-based expiry (unknown interval)
- Manual invalidation (unknown mechanism)

**Risk**: Stale snapshots may have outdated dependencies. Without clear invalidation control, this requires monitoring.

### Q4: How much time does snapshotting save?

Estimated savings for common stacks:

| Stack | Cold Install Time | With Snapshot |
|---|---|---|
| Java 21 + Maven deps | ~3-4 min | ~15-30 sec |
| Node 20 + npm ci | ~2-3 min | ~10-20 sec |
| Python 3.11 + pip | ~1-2 min | ~10-15 sec |
| Docker + compose | ~1-2 min | ~10-20 sec |
| **Total (all stacks)** | **~10-12 min** | **~1-2 min** |

_These are rough estimates based on GitHub Actions runner performance. Actual savings depend on dependency volume and network conditions._

### Q5: Is `snapshot` generally available?

As of April 2026, `snapshot` is listed in the official documentation as a supported key, but detailed behavior around invalidation and multi-stack scenarios is not fully documented. Treat as **preview/beta** — test in a non-critical repository first.

---

## `snapshot` vs. `actions/cache`

Standard `actions/cache` is also available in setup steps, but they serve different purposes:

| Feature | `snapshot: true` | `actions/cache` |
|---|---|---|
| Scope | Full environment image | Specific directories |
| Restore speed | Fast (OS-level) | Fast (tar extraction) |
| Control | Automatic | Manual key management |
| Per-stack | No | Yes (multiple cache steps) |
| Invalidation control | Opaque | Cache key management |

### Using `actions/cache` as a snapshot alternative

```yaml
      - name: Cache Maven dependencies
        uses: actions/cache@v4
        with:
          path: ~/.m2/repository
          key: maven-${{ hashFiles('**/pom.xml') }}
          restore-keys: maven-

      - name: Cache npm dependencies
        uses: actions/cache@v4
        with:
          path: ~/.npm
          key: npm-${{ hashFiles('**/package-lock.json') }}
          restore-keys: npm-
```

This approach:
- Is fully documented and stable
- Provides deterministic cache keys
- Saves 60-80% of dependency download time (tools still install)
- Works today without any experimental features

---

## Recommendation

| Scenario | Recommendation |
|---|---|
| Want maximum speed with minimal setup | Enable `snapshot: true` and monitor for staleness |
| Need deterministic, controlled caching | Use `actions/cache` with explicit cache keys |
| Multi-stack repo where all stacks are always needed | `snapshot: true` is the best fit |
| Multi-stack repo where only one stack runs per session | Combine file detection (Approach 1) with `actions/cache` |

---

## Example: Optimized Multi-Stack Setup with Caching

```yaml
jobs:
  copilot-setup-steps:
    runs-on: ubuntu-latest
    snapshot: true
    steps:
      - uses: actions/checkout@v4

      - name: Detect active stacks
        id: detect
        run: |
          echo "java=$(test -f backend/pom.xml && echo true || echo false)" >> $GITHUB_OUTPUT
          echo "node=$(test -f frontend/package.json && echo true || echo false)" >> $GITHUB_OUTPUT
          echo "python=$(test -f ml/requirements.txt && echo true || echo false)" >> $GITHUB_OUTPUT

      - name: Cache Maven
        if: steps.detect.outputs.java == 'true'
        uses: actions/cache@v4
        with:
          path: ~/.m2/repository
          key: maven-${{ hashFiles('backend/pom.xml') }}

      - name: Set up Java
        if: steps.detect.outputs.java == 'true'
        uses: actions/setup-java@v4
        with:
          java-version: '21'
          distribution: 'temurin'

      - name: Maven offline
        if: steps.detect.outputs.java == 'true'
        run: mvn dependency:go-offline -f backend/pom.xml

      # (Repeat pattern for Node and Python)
```

**Sources**: [Customizing the development environment](https://docs.github.com/en/copilot/customizing-copilot/customizing-the-development-environment-for-copilot-coding-agent) · [actions/cache](https://github.com/actions/cache)
