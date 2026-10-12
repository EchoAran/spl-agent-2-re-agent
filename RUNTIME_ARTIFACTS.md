# Runtime Artifacts Guide

This repository has two runtime systems:

- `spl_agent`: SPL tree build and Q&A service.
- `multi_agent_interview`: interview orchestration that calls `spl_agent`.

## Cache And Log Directories

- `spl_agent/.spl_cache/`
  - Created by `spl_agent` when running `spl-run` or `spl-api`.
  - Stores source snapshots, `spl_tree.json`, exported `.spl` files, and `llm_io.jsonl`.
  - Safe to delete. It will be rebuilt on next run.

- `multi_agent_interview/backend/runtime/`
  - Created by `multi_agent_interview` backend.
  - Stores interview session cache and SPL cache used by the respondent agent.
  - Safe to delete when no running backend process is using it.

## Legacy Name `.spl_i`

Historically, interview mode wrote SPL cache to a root-level `.spl_i/`.
The active flow now writes to:

- `multi_agent_interview/backend/runtime/spl_cache/`

If `.spl_i/` appears from old runs, it can be removed safely.

## Clean-Up Rule

Do not commit runtime artifacts:

- `.spl_cache/`
- `.spl_i/`
- `multi_agent_interview/backend/runtime/`
- any `spl_agent/.spl_cache*` temporary cache variants
