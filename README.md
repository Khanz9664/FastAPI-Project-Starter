# FastAPI Project Starter 🚀

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

## Features ✨
- JWT Authentication & Authorization
- Async PostgreSQL with SQLAlchemy 1.4+
- Docker & Docker Compose ready
- Swagger & ReDoc documentation
- Pytest integration with test coverage
- Secure password hashing (bcrypt)
- Modular project structure with:
  - Core configuration
  - Database models
  - Dependency injection
  - Routers for API endpoints
  - Schemas for data validation

## Project Structure 🗂️
```
project/
├── app/
│   ├── core/        # Configuration and security
│   ├── database/    # Database models and sessions
│   ├── dependencies/ # Authentication and utilities
│   ├── routers/     # API endpoints (users, auth, etc)
│   ├── schemas/   # Pydantic models
│   └── main.py      # Application entry point
├── tests/           # Unit and integration tests
├── migrations/      # Alembic migration scripts
├── Dockerfile       # Container configuration
└── docker-compose.yml # Multi-container setup
```

## New/Updated Sections

### Database Migrations
```bash
# Initialize migrations
alembic init -t async migrations

# Create new migration
alembic revision -m "create_users_table" --autogenerate

# Upgrade database
alembic upgrade head
```

### Environment Variables
Add these to your `.env` file:
```env
DATABASE_URL=postgresql+asyncpg://user:password@localhost/dbname
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
TEST_DATABASE_URL=postgresql://test_user:test_password@localhost/test_db
```

### API Endpoints
**Authentication**
```bash
POST /api/auth/token
Content-Type: application/x-www-form-urlencoded
```

**Users Management**
```bash
POST /api/users/ 
Content-Type: application/json
{
  "email": "user@example.com",
  "password": "securepassword",
  "full_name": "John Doe"
}
```

### Testing
```bash
# Run tests with coverage
pytest --cov=app tests/

# Run specific test file
pytest tests/test_main.py
```

### Production Deployment
```bash
# Using Docker
docker-compose -f docker-compose.prod.yml up --build

# Gunicorn with Uvicorn workers
gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:80
```

## Security Enhancements
- Password hashing with bcrypt (salt rounds: 12)
- Rate limiting on authentication endpoints
- CORS configured with allowed origins
- Security headers middleware included

---

### 📫 Connect with Me

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
