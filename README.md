# FastAPI Project Starter 🚀

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

A production-ready FastAPI template featuring JWT authentication, async PostgreSQL integration, Docker support, modular architecture, and built-in testing. Designed for scalable and secure API development.

---

## Features

- JWT authentication & authorization
- Async PostgreSQL with SQLAlchemy
- Docker & Docker Compose support
- Interactive API docs (Swagger & ReDoc)
- Pytest integration for unit testing
- Secure password hashing (bcrypt)
- Modular structure (config, models, dependencies, routers, schemas)
- CORS and security headers middleware

---

## Project Structure

```
FastAPI-Project-Starter/
├── app/
│   ├── core/          # Configurations & security settings
│   ├── database/      # Database models and session
│   ├── dependencies/  # Authentication and reusable dependencies
│   ├── routers/       # API endpoints (users, items, etc.)
│   ├── schemas/       # Pydantic models for data validation
│   └── main.py        # Application entry point
├── tests/             # Pytest-based test suite
├── Dockerfile         # Container configuration
├── docker-compose.yml # Multi-container setup
└── requirements.txt   # Python dependencies
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Khanz9664/FastAPI-Project-Starter.git
cd FastAPI-Project-Starter
```

### 2. Configure Config Variables

fastapi-project/app/core/config.py

```env
DATABASE_URL=postgresql+asyncpg://user:password@localhost/dbname
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
TEST_DATABASE_URL=postgresql://test_user:test_password@localhost/test_db
```

### 3. Run with Docker

```bash
docker-compose up --build
```

### 4. Run the App Locally

```bash
uvicorn app.main:app --reload
```

---

## API Endpoints

- **Authentication**
  - `POST /api/auth/token` (form: username, password)
- **User Management**
  - `POST /api/users/` (register new user)
  - `GET /api/users/me` (get current user info)
- **Items**
  - `GET /api/items/` (list example items)

Interactive docs available at `/docs` and `/redoc`.

---

## Testing

Run all tests:

```bash
pytest --cov=app tests/
```

Run a specific test file:

```bash
pytest tests/test_main.py
```

---

## Security

- Passwords hashed with bcrypt
- JWT-based authentication
- CORS configuration via environment
- Security headers middleware

---

## License

MIT License

---

## Author & Contact

<p align="center">
  <a href="https://instagram.com/shaddy9664">
    <img src="https://img.shields.io/badge/Instagram-%23E4405F.svg?logo=Instagram&logoColor=white" alt="Instagram"/>
  </a>
  <a href="https://linkedin.com/in/shahid-ul-islam-13650998">
    <img src="https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white" alt="LinkedIn"/>
  </a>
  <a href="https://x.com/Shaddy9664">
    <img src="https://img.shields.io/badge/X-black.svg?logo=X&logoColor=white" alt="X"/>
  </a>
  <a href="https://khanz9664.github.io/portfolio/">
    <img src="https://img.shields.io/badge/Portfolio-green" alt="Portfolio"/>
  </a>
  <a href="https://github.com/Khanz9664">
    <img src="https://img.shields.io/badge/Github-red" alt="Github"/>
  </a>
</p>

---
