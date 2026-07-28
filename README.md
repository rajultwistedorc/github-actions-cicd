# GitHub Actions CI/CD Demo

Flask REST API with Prometheus metrics, Docker multi-stage build, nginx reverse proxy, and GitHub Actions pipelines.

## Architecture

```text
Developer -> PR -> [PR Check: lint + test]
                -> merge main -> [CI: lint, test, docker push]
                              -> [CD: SSH deploy to server]

Internet -> nginx:80 -> Flask app:5000
                      -> redis:6379
```

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/health` | Health check |
| GET | `/metrics` | Prometheus metrics |
| GET | `/api/v1/users` | List users |
| GET | `/api/v1/users/:id` | Get user |
| POST | `/api/v1/users` | Create user |

## Local development

```bash
pip install -r app/requirements.txt
cd app && pytest -v tests/
make run
curl http://localhost:8080/health
```

## GitHub Secrets

| Secret | Purpose |
|--------|---------|
| `DOCKERHUB_USERNAME` | Docker Hub user |
| `DOCKERHUB_TOKEN` | Docker Hub token |
| `DEPLOY_HOST` | Deployment server |
| `DEPLOY_USER` | SSH user |
| `DEPLOY_SSH_KEY` | Private SSH key |

## License

MIT
