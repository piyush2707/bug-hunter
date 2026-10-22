# Review checklist

Use selectively; do not mechanically report every category.

## Logic and boundaries
- Off-by-one conditions; incorrect loop exits or returns
- Empty collections, zero, negative values, maximum values, null/missing fields
- Incorrect boolean operators, precedence, default values, timezone assumptions
- State transitions that skip, duplicate, or reorder work

## Errors and resources
- Exceptions swallowed or misclassified
- Failure paths that leave partial writes or inconsistent state
- Retries without bounds, backoff, or idempotency
- Missing timeout, cancellation, cleanup, or transaction rollback
- Fallback behavior that masks a real failure

## Security and privacy
- Authorization checked on the wrong object or after a sensitive action
- Trusting client-controlled identity, role, price, path, or tenant ID
- Injection, path traversal, unsafe deserialization, or secret leakage
- Validation that is bypassable through alternate entry points
- Sensitive data in logs, errors, URLs, or generated artifacts

## Concurrency and distributed systems
- Check-then-act races
- Shared mutable state without synchronization
- Duplicate event processing and non-idempotent handlers
- Cache invalidation and stale reads
- Ordering assumptions across async work or queues

## Interfaces and compatibility
- Request/response schema mismatch
- Incorrect status codes or error shape
- Breaking changes to public APIs, configuration, or serialized data
- Dependency/version assumptions not supported by the project
- Mismatch between documented and actual behavior

## Tests
- Tests assert implementation details but not user-visible behavior
- Missing regression case for the reported trigger
- Mocking away the boundary where the defect occurs
- Async tests that do not await work or reliably clean up
- Tests that pass only because fixtures omit realistic edge cases

## Signal quality
Before reporting, ask:
1. Can I name a concrete trigger?
2. Can I explain the incorrect behavior from code evidence?
3. Is the impact meaningful and not merely stylistic?
4. Is this introduced by the change, or is the changed code exposing it?
5. Would a maintainer know what to do next?
If any answer is no, investigate further or omit the finding.
