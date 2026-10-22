# Instructions for Claude Code

Project: `ai-voice-service/` inside `talelzakhama/RandomProjects`.

1. Read README.md and docs/*.md before making architectural assumptions. These docs are **drafts**.
2. Make small changes in feature branches; open a pull request for human review. Do not merge to main without approval.
3. Prefer Python 3.12+, type hints, FastAPI, pytest and modular interfaces. Keep voice-provider calls behind adapters.
4. For now, prioritize a mock call flow and tests; do not sign up for paid services, buy phone numbers, deploy, or contact customers without authorization.
5. No real customer PII, secrets, tokens, recordings or private business data in git or test fixtures. Use synthetic values.
6. Never log full phone numbers or transcripts by default; design explicit consent, retention and redaction before any live calls.
7. Do not claim real appointment booking, prices, emergency response or guaranteed outcomes.
8. Every code change should include relevant tests and a concise PR description with validation, risks and rollback.
9. If a decision changes scope, cost, infrastructure or privacy, propose a documentation change first.
10. ChatGPT and Claude Code do not directly communicate; GitHub files/issues/PRs are the shared source of truth.
