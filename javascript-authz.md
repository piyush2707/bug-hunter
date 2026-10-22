# Example: authorization uses a client-supplied owner

## Fixture

```javascript
async function getInvoice(req, db) {
  const invoiceId = req.params.invoiceId;
  const ownerId = req.query.ownerId;
  return db.invoice.findFirst({
    where: { id: invoiceId, ownerId }
  });
}
```

## Expected review signal

- **Severity:** High if this endpoint exposes invoices without independently binding `ownerId` to the authenticated principal; otherwise verify surrounding middleware before reporting
- **Location:** the query construction
- **Trigger:** an authenticated caller supplies another user's `ownerId`
- **Impact:** cross-user invoice access if no upstream authorization constraint exists
- **Suggested fix:** derive owner/tenant identity from the authenticated server-side principal and enforce authorization at the data boundary

## Important caveat

This is intentionally conditional. An agent must inspect middleware and the call path before treating it as a confirmed vulnerability.
