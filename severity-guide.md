# Severity guide

Severity describes impact if the defect is triggered, not how easy it was to spot.

| Severity | Use when | Typical examples |
|---|---|---|
| Critical | Broad compromise, irreversible loss, or core service unavailable with no reasonable workaround | Unauthenticated remote code execution in a widely exposed service |
| High | Serious security boundary bypass, major corruption, or widespread core workflow failure | Cross-tenant data exposure; all payments calculated incorrectly |
| Medium | Important but bounded failure, common case broken, or practical workaround exists | Valid users cannot access a common workflow; retry duplicates a bounded operation |
| Low | Narrow edge case with limited consequence and a concrete failure | One documented optional input causes a recoverable error |

## Calibration rules

- Do not assign severity based solely on scary terminology.
- Security findings require a plausible attacker capability and an affected boundary.
- Consider exposure, affected users, exploitability, and reversibility.
- A crash is not automatically Critical or High.
- If impact depends on an unknown deployment detail, state the assumption and lower confidence.
- When uncertain between two levels, choose the lower one and explain why.
