# Example: early return inside a loop

## Fixture

```python
def find_user(users, target_id):
    for user in users:
        if user["id"] == target_id:
            return user
        return None
```

## Expected review signal

- **Severity:** Medium
- **Location:** the `return None` line inside the loop
- **Trigger:** the first item has a different ID and a later item matches
- **Impact:** valid users after the first list item cannot be found
- **Suggested fix:** dedent `return None` so it runs after the loop

## Why this is actionable

The failure path is deterministic and the incorrect control flow is visible in the fixture.
