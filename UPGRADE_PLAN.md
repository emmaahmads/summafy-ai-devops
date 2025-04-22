| Day | Task                        | Description                                                        | Definition of Done (DoD)                                         |
|-----|-----------------------------|--------------------------------------------------------------------|------------------------------------------------------------------|
| 1   | Code Audit & Structure Review | Audit existing code, identify reuse patterns, and propose module separation | Common utilities extracted and imported correctly                |
| 1   | GenAI Backend Abstraction   | Support multiple GenAI backends (OpenAI, Bedrock, vLLM) via config | Backend switchable with a config value                           |
| 2   | Secrets Refactor            | Move hardcoded API keys/credentials to AWS SSM or Secrets Manager  | Secrets retrieved securely, no plaintext in code                 |
| 2   | Summarizer Testing          | Add unit tests for summarizer using mocked APIs                    | >80% coverage with deterministic mock behavior                   |
| 3   | Improve Step Function ASL   | Add retries, timeouts, and error handling to state machine         | Error paths and retries defined; validated via simulation        |
| 3   | IAM Role Review             | Minimize Lambda permissions                                        | Least privilege applied; IAM policy reviewed and updated         |
| 4   | CI/CD Pipeline              | GitHub Actions workflow for lint, test, and SAM deploy             | Workflow auto-deploys on push to main                            |
| 4   | Dev/Staging Profiles        | Add .samconfig.toml for dev, staging, prod                         | Different envs deployable without changing template              |
| 5   | Local E2E Test Harness      | Add CLI/script to run the full workflow locally with mocks         | Simulated end-to-end test possible from local shell              |
| 6   | Containerize Summarizer     | Build Docker image for summarizer (e.g. vLLM) for local or ECR use | Image builds and runs locally, optionally with GPU               |
| 7   | Observability – Logging & Tracing | Structured logs, correlation IDs, and enable X-Ray in Lambdas     | JSON logs with trace info; X-Ray dashboard available             |
| 7   | Alerting & Monitoring       | Create CloudWatch alarms for failures; optional Grafana dashboard  | Alert sends via SNS/email; basic dashboard visible               |
| 8   | Minimal Frontend / Public API | Build simple UI or HTTP endpoint for summary upload + view        | File can be uploaded and summary retrieved via UI or curl        |
| 9   | Documentation Polish        | Update README with all setup instructions and diagrams             | README reflects final structure, APIs, and dev process           |
| 10  | Demo Walkthrough + Release  | Record Loom video walkthrough and tag repo release                 | Walkthrough recorded and version tagged as v1.0                  |