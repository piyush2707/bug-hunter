# Example: unbounded retry

## Fixture

```python
def fetch_with_retry(fetch):
    while True:
        try:
            return fetch()
        except TemporaryError:
            continue
```

## Expected review signal

- **Severity:** Medium when `TemporaryError` can persist and callers expect bounded latency
- **Location:** the unbounded loop
- **Trigger:** every call raises `TemporaryError`
- **Impact:** request never returns, potentially tying up a worker indefinitely
- **Suggested fix:** impose a retry limit, use appropriate backoff, and surface the final failure

## Important caveat

Confirm the exception semantics and caller timeout expectations before final severity assignment.
