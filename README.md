# Module 13: FastAPI JWT Authentication

## 📌 Overview
This project implements JWT-based authentication using FastAPI.  
Users can register, login, and receive a JWT token for authentication.

---

## 🚀 Features

- User Registration (/users/register)
- User Login (/users/login)
- Password hashing (secure)
- JWT token generation
- Frontend pages (Register & Login)
- Automated testing using pytest
- CI/CD using GitHub Actions
- Docker support

---

## 🛠️ Tech Stack

- FastAPI
- SQLite
- SQLAlchemy
- Pydantic
- JWT (python-jose)
- Passlib (password hashing)
- Pytest
- Docker

---

## ▶️ How to Run

### 1. Clone repo

```bash
git clone https://github.com/sm3676/module13-fastapi-jwt
cd module13-fastapi-jwt


2. Install dependencies

pip install -r requirements.txt

3. Run backend

uvicorn app.main:app --reload
Open:
http://127.0.0.1:8000/docs

4. Run frontend

python -m http.server 5500

Open:

http://localhost:5500/register.html
http://localhost:5500/login.html


5. Run tests

pytest

🧪 Testing
Register test (dynamic email)
Login test (after register)
Calculation tests

All tests pass successfully in GitHub Actions.

🐳 Docker

Build image:

docker build -t module13-app .

Run container:

docker run -p 8000:8000 module13-app


🔐 Security
Passwords hashed using Passlib
JWT tokens used for authentication
Duplicate user prevention

👩‍💻 Author

Sharvani Rao Mucharla



2. Install dependencies
