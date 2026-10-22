# Contributing

Thanks for helping make Bug Hunter more precise and useful.

## Good contributions

- A reproducible bug pattern with a minimal fixture
- A checklist improvement grounded in real failure modes
- Better severity calibration or clearer reporting
- Tests that prevent regressions in repository tooling
- Compatibility fixes for documented agent environments

## Pull request checklist

- [ ] Explain the problem and why it matters.
- [ ] Keep examples minimal and remove secrets or proprietary data.
- [ ] Distinguish confirmed defects from conditional scenarios.
- [ ] Run `python3 tests/check_examples.py`.
- [ ] Update documentation when behavior or compatibility guidance changes.
- [ ] Do not add telemetry, network calls, or destructive automation without explicit discussion.

## Scope and style

Prefer small, focused changes. Do not add speculative findings just to increase the number of reported issues. Bug Hunter is review-only by default.
