# 🚀 FastAPI Project Starter  
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com)  
[![Python](https://img.shields.io/badge/Python-3.9+-brightgreen?style=for-the-badge&logo=python)](https://www.python.org)  
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](https://opensource.org/licenses/MIT)

> A production-ready FastAPI template with JWT authentication, async PostgreSQL, Docker support, and modular architecture. Built for secure, scalable API development.

---

## 📦 Features

| Feature                | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| 🔐 Authentication       | JWT token-based authentication with bcrypt password hashing                  |
| 🧱 Architecture         | Modular structure with separation of concerns (config, models, routers)    |
| 🐍 Async PostgreSQL    | SQLAlchemy + asyncpg for non-blocking database operations                  |
| 🐳 Docker              | Containerized setup with Docker Compose                                    |
| 🧪 Testing              | Pytest with coverage reports                                               |
| 📜 Docs                | Auto-generated Swagger (`/docs`) and ReDoc (`/redoc`)                      |
| 🔐 Security             | CORS middleware, rate limiting, and secure headers                          |

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

### 4. Run with Docker (Recommended)
```bash
docker-compose up --build
```

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
