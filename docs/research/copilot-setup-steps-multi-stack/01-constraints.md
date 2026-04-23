# 01 — Hard Constraints of `copilot-setup-steps.yml`

> **Sources**: [Customizing the development environment for Copilot coding agent](https://docs.github.com/en/copilot/customizing-copilot/customizing-the-development-environment-for-copilot-coding-agent) · [About Copilot coding agent](https://docs.github.com/en/copilot/copilot-individual/about-github-copilot-individual)

---

## 1. File Location and Branch

| Constraint | Detail |
|---|---|
| **File path** | `.github/workflows/copilot-setup-steps.yml` (exact name required) |
| **Branch** | Must exist on the **default branch** of the repository |
| **Effect** | If the file is absent, Copilot still runs but with no pre-installation |

## 2. Job Name

The workflow **must contain exactly one job** and it **must be named `copilot-setup-steps`**. Any other job name is silently ignored by the Copilot runner orchestrator.

```yaml
jobs:
  copilot-setup-steps:   # ← This exact name is required
    runs-on: ubuntu-latest
    steps: [...]
```

## 3. Allowed Top-Level Job Keys

Only the following keys are supported inside the `copilot-setup-steps` job. All other standard Actions job keys (e.g., `strategy`, `needs`, `outputs`) are **ignored or unsupported**.

| Key | Supported | Notes |
|---|---|---|
| `steps` | ✅ | Full step syntax supported |
| `runs-on` | ✅ | Standard runner labels |
| `permissions` | ✅ | Standard GITHUB_TOKEN permissions |
| `services` | ✅ | Docker sidecar containers |
| `snapshot` | ✅ | Environment caching (see `04-snapshot-deep-dive.md`) |
| `timeout-minutes` | ✅ | **Maximum 59 minutes** — hard cap |
| `strategy` / `matrix` | ❌ | Not supported |
| `needs` | ❌ | Only one job allowed |
| `outputs` | ❌ | No inter-job data passing |
| `environment` | ❌ | Not documented as supported |
| `concurrency` | ❌ | Managed by Copilot orchestrator |

## 4. Timeout Hard Cap

```yaml
jobs:
  copilot-setup-steps:
    timeout-minutes: 59   # Maximum allowed — values > 59 are rejected
```

This means the **entire serial setup** for all stacks must complete within 59 minutes. With even modest multi-stack installs (Java + Node + Python + Docker) this cap can become a real constraint.

## 5. No Multi-Job Parallelism

There is no mechanism to run setup steps in parallel. The single `copilot-setup-steps` job runs all steps serially. This is the root cause of the cumulative setup time problem described in the issue.

## 6. Runner Availability

Standard GitHub-hosted runners are available:

| Runner | Cores | RAM | Notes |
|---|---|---|---|
| `ubuntu-latest` | 2 | 7 GB | Default, cheapest |
| `ubuntu-22.04-4-core` | 4 | 15 GB | Faster I/O; costs ~2× more |
| `ubuntu-22.04-8-core` | 8 | 30 GB | For heavy parallel installs |
| Self-hosted | Varies | Varies | Custom image possible |

Larger runners reduce wall-clock time for CPU/IO-bound installs but do **not** change the serial execution model.

## 7. Secrets and Permissions

- Secrets are available via `${{ secrets.NAME }}` exactly as in normal workflows
- GITHUB_TOKEN permissions can be scoped with `permissions:`
- **Key limitation**: The GITHUB_TOKEN in setup steps runs with the permissions of the **Copilot app**, not the triggering user. Accessing private registries or writing repo content requires explicit permission grants.

## 8. Context Variables Available

The standard GitHub Actions [context objects](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/accessing-contextual-information-about-workflow-runs) are available during setup steps:

| Context | Available? | Useful for dynamic routing? |
|---|---|---|
| `github.event` | ⚠️ Partial | See `03-event-payload-access.md` |
| `github.repository` | ✅ | Repo name/owner |
| `github.ref` | ✅ | Branch/ref being worked on |
| `env.*` | ✅ | Environment variables |
| `vars.*` | ✅ | Repository/org variables |
| `secrets.*` | ✅ | Repository secrets |

## 9. What Cannot Be Changed

- **Number of jobs**: Always exactly one
- **Execution model**: Always serial (no parallelism)
- **Timeout ceiling**: Hard cap at 59 minutes
- **File name/location**: Fixed at `.github/workflows/copilot-setup-steps.yml`
- **When setup runs**: Always before every Copilot session — cannot be skipped for individual tasks

## Summary

These constraints mean the optimization problem is fundamentally about **doing less in serial**, not about restructuring the workflow. Every viable approach in `02-approaches.md` must work within the single-job, serial-step, 59-minute limit.
