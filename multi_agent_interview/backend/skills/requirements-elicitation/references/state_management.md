# State Management

This document defines the script-based state persistence system for maintaining interview framework across execution sessions.

## Overview

The state management system enables the skill to maintain continuity across multiple execution sessions by persisting the interview framework through skill-bundled scripts. This is essential when the skill cannot rely on runtime context injection.

## Architecture

### Storage Structure
State is persisted through skill scripts:
- `scripts/persist_framework_state.py` for save/load
- `scripts/clear_framework_state.py` for cleanup

The actual temp storage directory is created by script at:
- `{system_temp}/requirements_elicitation_state/{session_id}.json`

### Session Identification
- **Session ID Source**: runtime-provided opaque identifier
- **Rule**: use the exact `session_id` passed by runtime as script input
- **Path Safety**: scripts sanitize `session_id` for filename generation

### State Components
1. **Framework State File** (`{session_id}.json`): Complete interview framework matching `assets/interview_framework_schema.json`

## Operational Flow

### State Loading (Step 0)
1. Call `persist_framework_state.py --action load --session-id <id>`
2. If `exists=true`, validate and restore framework
3. If not found or invalid, proceed as new session

### State Persistence (Step 8)
1. After each state-changing operation, call:
   `persist_framework_state.py --action save --session-id <id> --framework-json <json>`
2. Use script output as source of truth for whether save succeeded

### State Cleanup (Completion)
1. After successful summarization, call:
   `clear_framework_state.py --action clear --session-id <id>`
2. If cleanup fails, surface error and retry once

## Error Handling

### Recovery Strategies
- **Framework Corruption**: Reinitialize from schema template
- **Missing State File**: Start as new session state
- **Storage Full**: Surface error and skip persistence for current turn

### Concurrency Protection
- Use atomic file operations (write to temp, then rename)
- Implement retry logic for transient failures
- Log conflicts but continue execution

## Implementation References

- Storage rules: `references/state_storage_rules.md`
- Lifecycle management: `references/state_lifecycle.md`
- Cleanup procedures: `references/state_cleanup.md`
