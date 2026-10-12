# State Cleanup Procedures

This document defines the procedures for cleaning up the session state file after interview completion.

## Cleanup Triggers

### Primary Trigger
**Interview Completion**: When phase reaches `complete` and summarization succeeds

**Conditions**:
- Framework phase == "complete"
- Summarization output generated successfully
- No pending operations requiring state

### Secondary Triggers
None in this skill runtime. Cleanup is only required at interview completion.

## Cleanup Process

### Standard Completion Cleanup

#### Step 1: Pre-Cleanup Validation
1. Verify interview is truly complete
2. Confirm summarization output was generated
3. Prepare current `session_id`

#### Step 2: Script Cleanup
1. Call `scripts/clear_framework_state.py --action clear --session-id <id>`
2. Treat script JSON output `deleted=true/false` as cleanup result

### Error Handling

#### Cleanup Failure Scenarios
- **Permission Denied**: retry once and surface failure
- **Concurrent Access**: retry once and surface failure

#### Failure Recovery
- Retry cleanup once on next invocation
- Surface error for manual follow-up
