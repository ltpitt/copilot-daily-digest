# 03 — Event Payload Access in `copilot-setup-steps`

> **Key question**: Can setup steps read the triggering issue/PR title, body, or labels — and use that data to decide which stacks to install?

---

## Background

When Copilot is assigned to an issue or PR, it triggers the `copilot-setup-steps` job before starting work. If that job can access the event payload (the issue title, body, labels, PR diff path patterns, etc.), it becomes possible to do fine-grained conditional setup.

---

## What GitHub Documents

The [official documentation](https://docs.github.com/en/copilot/customizing-copilot/customizing-the-development-environment-for-copilot-coding-agent) does not explicitly describe what `github.event` context is populated with during `copilot-setup-steps` execution. The workflow file is triggered by GitHub's Copilot orchestrator, not by a standard webhook event like `push` or `pull_request`.

---

## Analysis of Available Context

### `github.event_name`

During a Copilot-triggered setup, the event name is likely a proprietary internal event (not a standard Actions webhook event). This means `github.event_name` may not equal `issues` or `pull_request`.

### `github.event` object

Standard event payloads like `github.event.issue.labels` are only populated when the workflow is triggered by the corresponding webhook event. Since `copilot-setup-steps` is triggered by Copilot's internal orchestrator:

- **`github.event.issue.*`** — likely **empty or absent**
- **`github.event.pull_request.*`** — likely **empty or absent**
- **`github.event.label.*`** — likely **empty or absent**

### What IS reliably available

| Context | Available? | Notes |
|---|---|---|
| `github.repository` | ✅ Yes | Repo owner/name |
| `github.ref` | ✅ Yes | Ref being worked on |
| `github.sha` | ✅ Yes | Commit SHA |
| `github.actor` | ✅ Yes | Who triggered |
| `vars.*` | ✅ Yes | Repository variables |
| `secrets.*` | ✅ Yes | Repository secrets |
| `github.event.issue.*` | ❓ Unknown | Not documented |
| `github.event.*.labels` | ❓ Unknown | Not documented |
| `GITHUB_EVENT_PATH` file | ❓ Unknown | May be empty or minimal |

---

## Testing the Unknown

### Method 1: Dump the event payload

Add a step to `copilot-setup-steps.yml` that dumps the event context:

```yaml
      - name: Debug event context
        run: |
          echo "Event name: ${{ github.event_name }}"
          echo "Event path: $GITHUB_EVENT_PATH"
          cat $GITHUB_EVENT_PATH || echo "Event file empty or missing"
          echo "Issue number: ${{ github.event.issue.number }}"
          echo "Labels: ${{ toJson(github.event.issue.labels) }}"
```

Run this and observe the actual Copilot session output. This is the only reliable way to determine what is available.

### Method 2: GitHub REST API call

Even if the event payload is unavailable, setup steps can call the GitHub API to fetch issue/PR metadata:

```yaml
      - name: Fetch issue labels via API
        id: issue_labels
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          # GITHUB_REF for a Copilot session may be the issue number or PR number
          # This requires knowing the issue/PR number - which may not be available
          ISSUE_NUMBER="${{ github.event.issue.number }}"
          if [ -n "$ISSUE_NUMBER" ]; then
            LABELS=$(gh api repos/${{ github.repository }}/issues/$ISSUE_NUMBER \
              --jq '[.labels[].name] | join(",")')
            echo "labels=$LABELS" >> $GITHUB_OUTPUT
          fi
```

**Limitation**: This approach requires knowing the issue or PR number, which itself may only be available if `github.event.issue.number` is populated.

---

## What Community Experience Suggests

Based on GitHub Community discussions and the Copilot changelog:

1. **Copilot passes limited context**: The orchestrator appears to pass a minimal event payload focused on the session trigger (issue assignment, PR comment), but the structure is not publicly documented.

2. **The `GITHUB_EVENT_PATH` environment variable**: This standard Actions variable points to a JSON file containing the event payload. In Copilot-triggered runs, its contents may differ from standard webhook events.

3. **No official confirmation**: As of April 2026, GitHub has not published documentation confirming which fields in `github.event` are populated during Copilot setup steps.

---

## Workaround: Encode Stack Signal in Issue Title or Body

If event payload access turns out to be unreliable, a practical workaround is to **use a convention in issue titles or bodies** that the agent parses at startup (not in setup steps), and then self-installs. Alternatively, encoding stack info in repository variables (which ARE reliably available) is more robust.

### Convention-based example (in copilot-instructions.md)

```markdown
## Stack Detection

When you start working on an issue, check the issue title for stack tags:
- `[java]` or `[backend]` → Java/Spring Boot stack
- `[node]` or `[frontend]` → Node.js/React stack
- `[python]` or `[ml]` → Python/ML stack

If the required tooling is not installed, use sdkman/nvm/pyenv to install it.
```

---

## Recommendation

| Scenario | Recommendation |
|---|---|
| Want to test label routing | Add the debug step above to your `copilot-setup-steps.yml` and inspect real Copilot session output |
| Need reliable stack detection today | Use file-system detection (Approach 1 in `02-approaches.md`) |
| Can wait for GitHub to document this | Monitor the [Copilot changelog](https://github.blog/changelog/label/copilot/) for event payload access announcements |

---

## Open Questions for GitHub

1. What `event_name` does Copilot set when triggering `copilot-setup-steps`?
2. Is `GITHUB_EVENT_PATH` populated, and if so, what fields does it contain?
3. Is there a planned API or context variable to expose the triggering issue/PR number to setup steps?

These questions should be raised in [GitHub Community Discussions](https://github.com/orgs/community/discussions) or the GitHub Copilot feedback repository.

**Sources**: [GitHub Actions context](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/accessing-contextual-information-about-workflow-runs) · [Copilot coding agent docs](https://docs.github.com/en/copilot/customizing-copilot/customizing-the-development-environment-for-copilot-coding-agent)
