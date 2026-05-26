# FastAPI Production Boilerplate

<p align="center">
  <strong>Production-ready FastAPI boilerplate built for scalable, async-first backend systems.</strong>
</p>

<p align="center">
  JWT Authentication • RBAC • Redis • ARQ Workers • Docker • CI/CD • Observability
</p>

<p align="center">
  <a href="https://github.com/Khanz9664/FastAPI-Production-Boilerplate/actions/workflows/test.yml">
    <img src="https://github.com/Khanz9664/FastAPI-Production-Boilerplate/actions/workflows/test.yml/badge.svg" alt="CI">
  </a>
  <img src="https://img.shields.io/badge/python-3.12+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-async-success" alt="FastAPI">
  <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License">
</p>

---

## Overview

**FastAPI Production Boilerplate** is an opinionated, production-ready backend foundation for building scalable APIs with FastAPI.

It provides a clean architecture, async-first infrastructure, authentication, authorization, observability, background workers, Redis integration, Dockerized deployment, and CI/CD out of the box — allowing developers to focus on business logic instead of repetitive setup.

Unlike typical FastAPI starter templates, this repository prioritizes:

- production readiness
- maintainability
- observability
- security-first design
- async-native architecture
- developer experience

---

## Why This Boilerplate Exists

Most FastAPI starter projects stop at:

- CRUD endpoints
- basic JWT authentication
- minimal Docker setup

This repository goes further.

It is designed as a **microservice-ready monolith** with clean architectural boundaries and infrastructure patterns commonly used in production systems.

Features such as RBAC, Redis-backed background jobs, health probes, Prometheus metrics, pagination, CI/CD, and structured responses are built in from the start.

---

## Features

### API & Architecture

| Capability | Included |
|------------|----------|
| FastAPI + Pydantic v2 | ✓ |
| Layered Architecture | ✓ |
| Repository Pattern | ✓ |
| Dependency Injection | ✓ |
| API Versioning (`/api/v1`) | ✓ |
| Generic Pagination | ✓ |
| Sorting & Filtering | ✓ |
| Structured API Responses | ✓ |

### Authentication & Security

| Capability | Included |
|------------|----------|
| JWT Authentication | ✓ |
| Password Hashing (`bcrypt`) | ✓ |
| RBAC (Admin / Moderator / User) | ✓ |
| Route Permission Guards | ✓ |
| Rate Limiting | ✓ |
| Abuse Protection | ✓ |
| Unified Error Responses | ✓ |

### Infrastructure

| Capability | Included |
|------------|----------|
| PostgreSQL (Async SQLAlchemy) | ✓ |
| Redis Integration | ✓ |
| ARQ Async Workers | ✓ |
| Background Jobs | ✓ |
| Health Probes | ✓ |
| Prometheus Metrics | ✓ |

### Operations & Developer Experience

| Capability | Included |
|------------|----------|
| Docker Compose Stack | ✓ |
| Multi-stage Dockerfile | ✓ |
| GitHub Actions CI | ✓ |
| Alembic Migrations | ✓ |
| Pre-commit Hooks | ✓ |
| Black / Isort / Flake8 / Mypy | ✓ |
| Pytest Coverage | ✓ |

---

## Architecture

The project follows a layered architecture to maintain separation of concerns and long-term maintainability.

```mermaid
flowchart TD

Client[Client Request]
Router[API Router]
Service[Service Layer]
Repository[Repository Layer]
Database[(PostgreSQL)]

Redis[(Redis)]
Worker[ARQ Worker]

Client --> Router
Router --> Service
Service --> Repository
Repository --> Database

Service --> Redis
Redis --> Worker
Worker --> Database
```

### Request Flow

```text
Request
  ↓
Router
  ↓
Service
  ↓
Repository
  ↓
Database
```

This structure ensures:

- clean business logic separation
- reusable data access
- testability
- maintainability
- future microservice migration paths

---

## Technology Decisions

### Why ARQ Instead of Celery?

This project intentionally uses **ARQ** instead of Celery.

Celery is powerful, but introduces unnecessary complexity in fully asynchronous FastAPI systems due to its synchronous execution model.

ARQ provides:

- native `asyncio` support
- Redis-backed job queues
- lower overhead
- seamless async database access
- simpler developer experience

This keeps the entire stack consistently async-first.

---

## Quick Start

### Clone the repository

```bash
git clone https://github.com/Khanz9664/FastAPI-Production-Boilerplate.git

cd FastAPI-Production-Boilerplate
```

### Start the full stack

The recommended way to run the project is via Docker Compose.

```bash
docker compose up --build
```

This will start:

- FastAPI API server
- PostgreSQL database
- Redis cache
- ARQ worker process

Open:

```text
http://localhost:8000/docs
```

to access Swagger UI.

---

## Local Development

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure environment variables

Create a `.env` file:

```env
DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/app
REDIS_URL=redis://localhost:6379

SECRET_KEY=your-secret-key
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Run database migrations

```bash
alembic upgrade head
```

### Run FastAPI

```bash
uvicorn app.main:app --reload
```

### Run worker

```bash
arq app.worker.WorkerSettings
```

---

## Project Structure

```text
FastAPI-Production-Boilerplate/

app/
├── api/
│   └── v1/
│       ├── auth.py
│       ├── users.py
│       └── items.py
│
├── core/
│   ├── config/
│   ├── security.py
│   ├── limiter.py
│   └── redis.py
│
├── db/
│   ├── session.py
│   └── migrations/
│
├── middleware/
│
├── models/
│
├── repositories/
│
├── schemas/
│
├── services/
│
├── worker.py
│
└── main.py

tests/
.github/workflows/
docker-compose.yml
Dockerfile
```

---

## API Capabilities

### Authentication

JWT authentication with secure password hashing.

```http
POST /api/v1/auth/token
```

---

### Role-Based Access Control

Protect endpoints using role guards.

Example:

```python
Depends(RoleChecker([UserRole.ADMIN]))
```

Supported roles:

- `ADMIN`
- `MODERATOR`
- `USER`

---

### Pagination, Sorting & Search

Generic pagination system built into repositories.

Example:

```http
GET /api/v1/items?skip=0&limit=10
```

Search:

```http
GET /api/v1/items?search=phone
```

Sorting:

```http
GET /api/v1/items?sort_by=created_at&sort_order=desc
```

Response format:

```json
{
  "success": true,
  "message": "Items retrieved successfully",
  "data": {
    "items": [],
    "pagination": {
      "total": 100,
      "skip": 0,
      "limit": 10,
      "has_next": true
    }
  }
}
```

---

## Observability

### Health Probes

Kubernetes-ready health endpoints:

```http
GET /health
GET /live
GET /ready
```

---

### Metrics

Prometheus-compatible metrics:

```http
GET /metrics
```

Includes:

- request latency
- request counts
- application metrics

---

## Background Jobs

Background tasks are handled using ARQ workers.

Example workflow:

```text
User Registration
      ↓
Enqueue Welcome Email Task
      ↓
Redis Queue
      ↓
ARQ Worker
      ↓
Email Execution
```

---

## Testing

Run the full test suite:

```bash
pytest
```

Run with coverage:

```bash
pytest --cov=app
```

The project includes:

- API tests
- RBAC tests
- authentication tests
- rate limiting tests
- Redis mocking tests
- background worker tests

---

## CI/CD

GitHub Actions automatically validates:

- formatting
- linting
- type checking
- migrations
- tests
- Docker builds

Pipeline:

```text
Lint → Tests → Alembic → Docker Build
```

---

## Deployment Readiness

The boilerplate is designed for deployment in production environments.

Includes:

- Docker health checks
- non-root containers
- Redis-backed workers
- PostgreSQL readiness checks
- Prometheus metrics
- CI quality gates

Compatible with:

- Docker
- Kubernetes
- Railway
- Render
- Fly.io
- DigitalOcean

---

## Contributing

Contributions are welcome.

Before opening a pull request:

```bash
pre-commit run --all-files
```

Ensure:

```bash
pytest
```

passes successfully.

---

## License

This project is licensed under the MIT License.

See `LICENSE` for details.

---

## Author

**Shahid Ul Islam**

GitHub: https://github.com/Khanz9664

LinkedIn: https://linkedin.com/in/shahid-ul-islam-13650998

Portfolio: https://khanz9664.github.io/portfolio/
