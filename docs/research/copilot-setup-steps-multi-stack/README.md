# Copilot Setup Steps — Multi-Stack Optimization Research

> **For**: Lead developers managing multi-stack repositories with GitHub Copilot coding agent  
> **Purpose**: How to make `copilot-setup-steps.yml` dynamically adapt to the task at hand  
> **Last updated**: April 2026

---

## The Problem in One Paragraph

Every Copilot coding agent session runs `.github/workflows/copilot-setup-steps.yml` before the agent starts work. This single serial job installs all tooling for all stacks — even if the agent is only touching one. A Java backend + React frontend + Python ML repo can accumulate 10-15 minutes of setup time, consumes more secrets than necessary, and becomes a maintenance burden as stacks grow.

---

## Hard Limits (non-negotiable)

| Constraint | Value |
|---|---|
| Job name | Must be `copilot-setup-steps` |
| Number of jobs | Exactly **one** |
| Max timeout | **59 minutes** |
| Execution model | Serial steps only — no parallelism |
| Multi-job support | ❌ Not supported |
| Matrix strategies | ❌ Not supported |

See [01-constraints.md](01-constraints.md) for complete details.

---

## 5-Minute Decision Matrix

> Pick the row that matches your situation and follow the "Action" column.

| Situation | Recommended Action | Est. Setup Time After | Files |
|---|---|---|---|
| Simple repo (1-2 stacks) | Add `snapshot: true` + `actions/cache` | < 2 min | [04](04-snapshot-deep-dive.md) |
| Monorepo, not all stacks needed per task | File detection + `if:` guards | 2-4 min (subset only) | [02](02-approaches.md) |
| Monorepo, maintenance is the pain point | Composite actions per stack | Same as today, cleaner | [02](02-approaches.md) |
| All stacks needed, just need speed | `snapshot: true` + larger runner | < 2 min | [04](04-snapshot-deep-dive.md), [02](02-approaches.md) |
| Setup hitting 59-min timeout | File detection (reduce what runs) + 4-core runner | -50% or more | [02](02-approaches.md) |
| Want per-issue/PR routing | Wait — event payload access not confirmed | N/A | [03](03-event-payload-access.md) |

---

## Approaches Summary

| # | Approach | Time Saved | Complexity | Ready Today? |
|---|---|---|---|---|
| 1 | File detection + `if:` guards | Medium | Low | ✅ Yes |
| 2 | Repository variables | Low | Low | ✅ Yes |
| 3 | Issue/PR label routing | High (if it works) | Medium | ⚠️ Uncertain |
| 4 | Composite actions per stack | 0 (org only) | Medium | ✅ Yes |
| 5 | `snapshot: true` caching | Very High | Low | ⚠️ Preview |
| 6 | `services:` for infra | Low | Low | ✅ Yes |
| 7 | Larger runners | Low-Medium | None | ✅ Yes |
| 8 | Separate repos per stack | Very High | Very High | ✅ Architectural |
| 9 | Copilot instructions self-install | Medium | Low | ⚠️ Unreliable |
| 10 | Custom self-hosted runner images | Very High | High | ✅ If infra exists |

Full analysis: [02-approaches.md](02-approaches.md)

---

## Recommended Implementation Order

```
Step 1 (Quick Win, Low Risk):
  Add file-based stack detection + if: guards
  → Eliminates installs for stacks not present in this run
  → Details: 02-approaches.md § Approach 1

Step 2 (Quick Win, Low Risk):
  Add actions/cache for each detected stack
  → Cuts dependency download time by 60-80%
  → Details: 04-snapshot-deep-dive.md § actions/cache alternative

Step 3 (Maintenance Win):
  Extract each stack into a composite action
  → Stack teams own their own setup files
  → Details: 02-approaches.md § Approach 4

Step 4 (Speed Win, When Stable):
  Enable snapshot: true
  → Near-zero setup time for cached sessions
  → Details: 04-snapshot-deep-dive.md

Step 5 (Monitor):
  Watch for GitHub announcement on event payload in setup steps
  → If confirmed, add label-based routing for per-issue precision
  → Details: 03-event-payload-access.md
```

---

## Key Open Question

**Can setup steps read the triggering issue's labels?**

If yes → label-based routing (Approach 3) becomes the most powerful technique.  
If no → file-based detection (Approach 1) is the best available signal.

Current status: **Undocumented / uncertain.** See [03-event-payload-access.md](03-event-payload-access.md) for investigation method and workarounds.

---

## File Index

| File | Contents |
|---|---|
| [01-constraints.md](01-constraints.md) | Hard limits: job name, timeout, allowed keys, available context |
| [02-approaches.md](02-approaches.md) | All 10 approaches with YAML examples, pros/cons, and verdict |
| [03-event-payload-access.md](03-event-payload-access.md) | Can setup steps read issue/PR title, body, and labels? |
| [04-snapshot-deep-dive.md](04-snapshot-deep-dive.md) | `snapshot: true` feature analysis + `actions/cache` alternative |
| [05-real-world-examples.md](05-real-world-examples.md) | Public repos, patterns, and observed setup times |
| [06-recommendations.md](06-recommendations.md) | Ranked action plan with implementation sequence |

---

## Official Resources

- [Customizing the development environment for Copilot coding agent](https://docs.github.com/en/copilot/customizing-copilot/customizing-the-development-environment-for-copilot-coding-agent)
- [About GitHub Copilot coding agent](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-for-pull-requests/using-copilot-on-github)
- [GitHub Actions context objects](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/accessing-contextual-information-about-workflow-runs)
- [Creating composite actions](https://docs.github.com/en/actions/sharing-automations/creating-actions/creating-a-composite-action)
- [actions/cache](https://github.com/actions/cache)
- [GitHub Copilot changelog](https://github.blog/changelog/label/copilot/)
