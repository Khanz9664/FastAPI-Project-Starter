# FastAPI Project Starter 🚀

A production-ready FastAPI template with authentication, database integration, and Docker support.

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

## Features ✨

- ✅ JWT Authentication & Authorization
- 🐘 Async PostgreSQL with SQLAlchemy 1.4+
- 📦 Docker & Docker Compose ready
- 📄 Swagger & ReDoc documentation
- 🧪 Pytest integration
- 🔒 Secure password hashing
- 🧩 Modular project structure
- 🌐 CORS Middleware configured
- 📈 Production-ready configuration
- 🔄 Async database operations

## Installation 📥

### Prerequisites
- Python 3.9+
- PostgreSQL
- Docker (optional)

### Local Setup
```bash
# Clone repository
git clone https://github.com/yourusername/fastapi-project.git
cd fastapi-project

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Set environment variables
cp .env.example .env
# Update .env with your values

# Run database migrations (Alembic example)
alembic upgrade head

# Start server
uvicorn app.main:app --reload
```
# Docker Setup
```docker-compose up --build```
# API Documentation 📚
- Swagger UI: [http://localhost:8000/api/docs](https://swagger.io/docs/)
- ReDoc: http://localhost:8000/api/redoc

Usage Examples 🛠️

- Create User
```
POST /api/users/
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "secret123",
  "full_name": "John Doe"
}
```

- Authentication
```
POST /api/auth/token
Content-Type: application/x-www-form-urlencoded
username=user@example.com&password=secret123
```

- Access Protected Route
```
GET /api/users/me
Authorization: Bearer <access_token>
```

# Project Structure 🗂️
```
FastAPI Project Starter/
├── app/               # Main application code
│   ├── core/         # Configuration settings
│   ├── database/     # Database connection & models
│   ├── dependencies/ # Auth and other dependencies
│   ├── routers/      # API endpoint controllers
│   ├── schemas/      # Pydantic models
│   ├── utils/        # Helper functions
│   └── main.py       # Application entry point
├── tests/            # Test cases
├── migrations/       # Database migration scripts
├── Dockerfile        # Container configuration
└── docker-compose.yml# Multi-container setup
```

# Environment Variables ⚙️
- Create .env file with following variables:
```
DATABASE_URL=postgresql+asyncpg://user:password@localhost/dbname
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

# Running Tests 🧪
```
pytest tests/
```

# Deployment 🚀
- Production Server
```
uvicorn app.main:app --host 0.0.0.0 --port 80 --workers 4
```
- With Docker
```
docker-compose -f docker-compose.prod.yml up --build
```

# Contributing 🤝
- Fork the repository
- Create your feature branch (git checkout -b feature/amazing-feature)
- Commit your changes (git commit -m 'Add some amazing feature')
- Push to the branch (git push origin feature/amazing-feature)
- Open a Pull Request

# License 📄
- This project is licensed under the MIT License.

Made with ❤️ by **Shahid Ul Islam** 

_Machine Learning & Data Science Enthusiast_

GitHub: [http://github.com/Khanz9664](http://github.com/Khanz9664)
