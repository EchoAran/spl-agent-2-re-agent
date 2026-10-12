# State Storage Rules

This document defines the detailed rules for storing, retrieving, and managing state via skill scripts.

## State File Format

### `{session_id}.json`
Complete interview framework state conforming to `assets/interview_framework_schema.json`.

**Example Structure**:
```json
{
  "phase": "runtime",
  "current_topic_id": "user_requirements",
  "topics": [...],
  "open_questions": [...]
}
```

## Storage Rules

### Directory Structure
- **Base Path**: `{system_temp}/requirements_elicitation_state/`
- **Session Path**: `{system_temp}/requirements_elicitation_state/{session_id}.json`
- **Permissions**: Read/write for skill process

### File Naming
- State file extension is `.json`
- `session_id` must be sanitized to `[A-Za-z0-9_-]`
- Unsupported characters are stripped before path generation

### Size Limits
- **State File**: 5MB maximum

### Encoding
- All files: UTF-8 encoding
- JSON formatting: Pretty-printed with 2-space indentation
- Line endings: LF (\n) for cross-platform compatibility

## File Operations

### Atomic Writes
1. Write to temporary file: `{session_id}.json.tmp`
2. Validate JSON syntax
3. Rename to final state filename
4. Delete temporary file

### Read Operations
1. Check file existence
2. Read entire state file content
3. Parse JSON with error handling
4. Validate against framework schema

### Error Handling
- **File Not Found**: Treat as new session state
- **JSON Parse Error**: Log and use defaults
- **Permission Denied**: Log and continue with in-memory state
- **Disk Full**: Surface save failure and retry once

## Validation Rules

### Framework Validation
- Must conform to `interview_framework_schema.json`
- Required fields: `phase`, `current_topic_id`, `topics`, `open_questions`
- Phase must be one of: `start`, `runtime`, `complete`
