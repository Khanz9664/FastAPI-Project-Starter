# 🚀 Production-Ready FastAPI Boilerplate
[![Test FastAPI Application](https://github.com/Khanz9664/FastAPI-Project-Starter/actions/workflows/test.yml/badge.svg)](https://github.com/Khanz9664/FastAPI-Project-Starter/actions/workflows/test.yml)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com)  
[![Python](https://img.shields.io/badge/Python-3.12+-brightgreen?style=for-the-badge&logo=python)](https://www.python.org)  
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](https://opensource.org/licenses/MIT)

> **Async • Secure • Scalable • Dockerized**
> 
> A robust, battle-tested FastAPI template engineered for production. It combines modern async Python best practices with a highly modular architecture, giving you a deployment-ready foundation in seconds.

---

## ⚡ Feature Matrix

| Feature | Status | Description |
|---|---|---|
| **FastAPI + Pydantic V2** | ✅ | Blazing fast routing and strict schema validation |
| **Async PostgreSQL** | ✅ | SQLAlchemy 2.0 with `asyncpg` for non-blocking DB operations |
| **Authentication** | ✅ | Secure JWT token issuance with Bcrypt password hashing |
| **RBAC** | ✅ | Role-Based Access Control (Admin, Moderator, User) out of the box |
| **Pagination & Search** | ✅ | Native, generic offset pagination and text search in repositories |
| **Redis Caching** | ✅ | High-performance async caching via `redis.asyncio` |
| **ARQ Workers** | ✅ | Pure `asyncio` background job queue (No Celery overhead!) |
| **Rate Limiting** | ✅ | Built-in `slowapi` to prevent abuse (429 handling) |
| **Observability** | ✅ | `/health`, `/live`, `/ready` and Prometheus `/metrics` probes |
| **Dockerized** | ✅ | Multi-stage Dockerfile + Docker Compose for the entire stack |
| **CI/CD Quality Gates** | ✅ | GitHub Actions enforcing Pytest, Black, Isort, Flake8, and Mypy |

---

## 🏗️ Architecture Flow

```mermaid
graph TD
    Client([Client]) -->|HTTP Request| API[FastAPI App]
    API -->|JWT Validated| Auth[Security Dependency]
    Auth --> Router[API Router]
    
    subgraph Core Infrastructure
        Router -->|Delegates logic| Repo[Repository Pattern]
        Repo -->|Async ORM| DB[(PostgreSQL)]
        Router -->|Background Task| Queue{Redis Broker}
        Queue --> Worker[ARQ Async Worker]
        Worker -.->|DB Access| DB
    end
```

---

## 🤔 Why ARQ over Celery?
While Celery is the industry standard for background workers, it is fundamentally synchronous. Using Celery in a fully async FastAPI environment often leads to complex workarounds just to await database queries. 

We chose **[ARQ](https://arq-docs.helpmanual.io/)** (created by the author of Pydantic) because it is a natively `asyncio` job queue backed by Redis. This means your API and your Workers share the exact same `async/await` syntax, allowing seamless code reuse and significantly lower overhead.

---

## 📁 Project Structure

```
FastAPI-Project-Starter/
├── app/                  # Application source code
│   ├── core/           # Configuration, security, and global settings
│   │   └── config.py   # Environment variables and settings
│   │   └── security.py # JWT utilities and password hashing
│   ├── database/       # Database models and async session
│   │   └── models.py   # SQLAlchemy ORM models
│   │   └── session.py  # Async database session manager
│   ├── dependencies/   # Reusable dependency injectors
│   ├── routers/        # API endpoints (auth, users, items)
│   │   └── auth.py    # Authentication routes
│   │   └── users.py   # User management routes
│   │   └── items.py   # Example protected routes
│   ├── schemas/        # Pydantic models for data validation
│   └── main.py         # FastAPI app initialization
│
├── tests/              # Unit and integration tests
│   └── test_auth.py   # Authentication test suite
│   └── test_users.py  # User management tests
│
├── Dockerfile          # Production container configuration
├── docker-compose.yml  # Development environment (PostgreSQL + app)
├── requirements.txt    # Python dependencies
└── .env.example        # Example environment variables
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/Khanz9664/FastAPI-Project-Starter.git
cd FastAPI-Project-Starter
```

### 2. Configure Variables
Update values in config.py:
```bash
# app/core/config.py
DATABASE_URL=postgresql+asyncpg://user:password@localhost/dbname
TEST_DATABASE_URL=postgresql://test_user:test_password@localhost/test_db
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Docker Quick Start (Recommended)
Spin up the entire stack (API, PostgreSQL, Redis, Worker) instantly:
```bash
docker-compose up --build
```
Then visit [http://localhost:8000/docs](http://localhost:8000/docs) to view the auto-generated Swagger UI!

### 5. Run Locally
```bash
uvicorn app.main:app --reload
```

---

## 🧪 Testing

Run all tests with coverage:
```bash
pytest --cov=app tests/
```

Run specific test file:
```bash
pytest tests/test_auth.py
```

---

## 🔐 API Endpoints

### Authentication
- `POST /api/auth/token`  
  *Form data*: `username`, `password`  
  *Returns*: JWT access token

### User Management
- `POST /api/users/`  
  *Body*: `username`, `password`, `email`  
  *Creates*: New user account

- `GET /api/users/me`  
  *Requires*: Valid JWT token  
  *Returns*: Current user details

### Example Protected Route
- `GET /api/items/`  
  *Requires*: Authentication  
  *Returns*: List of example items

---

## 🛠️ Development Tools

- **Linting**: Use `flake8` or `black` for code formatting
- **Type Checking**: Run `mypy app/` for static type validation
- **Database Migrations**: Use `alembic` for schema changes

---

## 📦 Docker Commands

```bash
# Build and run containers
docker-compose up --build

# Stop containers
docker-compose down

# Run tests in container
docker-compose exec app pytest --cov=app tests/
```

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📨 Contact

- **Author**: Shahid Ul Islam  
- **GitHub**: [@Khanz9664](https://github.com/Khanz9664)  
- **LinkedIn**: [Profile](https://linkedin.com/in/shahid-ul-islam-13650998)  
- **Portfolio**: [khanz9664.github.io](https://khanz9664.github.io/portfolio/)
