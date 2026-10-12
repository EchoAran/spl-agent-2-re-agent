# State Lifecycle Management

This document defines the lifecycle of framework state persisted by skill scripts.

## Session Lifecycle Phases

### 1. Initialization Phase
**Trigger**: First execution or when no existing state found.

**Actions**:
1. Use runtime `session_id` as state key.
2. Call `persist_framework_state.py --action load --session-id <id>`.
3. If state file does not exist, initialize framework in memory from schema defaults.

**State File Location**:
- `{system_temp}/requirements_elicitation_state/{session_id}.json`

### 2. Runtime Phase
**Trigger**: After initialization until completion.

**Turn Rules**:
1. Turn start: load framework (`action=load`).
2. Apply structure/content updates in memory.
3. If state changed: save framework (`action=save`).

### 3. Completion Phase
**Trigger**: Interview reaches `complete` and summary is generated.

**Actions**:
1. Produce final summary output.
2. Call `clear_framework_state.py --action clear --session-id <id>`.
3. Ensure the session state file is deleted.

## State Recovery Process

### Recovery Steps
1. Call load script with current `session_id`.
2. If `exists=true`, parse and validate returned framework.
3. If invalid or missing, continue as new session.

### Recovery Failure Handling
- **Invalid framework JSON**: reinitialize from schema defaults.
- **Missing file**: treat as fresh session.
- **Script execution failure**: retry once, then continue with in-memory fallback.

## State Synchronization

### Rules
- Source of truth across turns is script-managed state file.
- In-memory state is per-turn working copy.
- Persist only through `persist_framework_state.py`.
- Cleanup only through `clear_framework_state.py`.
