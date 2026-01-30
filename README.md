"# ELS - Flask User Registration System

A modern, secure user registration and authentication system built with Flask. Includes user registration, login, password reset, and session management with a beautiful UI.

## ✨ Features

- **User Registration** - Sign up with username, email, and password
- **Secure Login** - Session-based authentication with password hashing
- **Password Reset** - Email-based password recovery with secure tokens
- **Protected Routes** - Dashboard only accessible to logged-in users
- **Responsive Design** - Beautiful, mobile-friendly UI with gradient styling
- **Docker Ready** - Dockerfile and docker-compose included
- **Production Ready** - Includes gunicorn and deployment guides

## 🚀 Quick Start

### Local Development
```bash
cd /workspaces/els
pip install -r requirements.txt
python app.py
```

### Docker
```bash
docker-compose up
```

Visit: **http://localhost:5000**

## 📋 Project Structure

```
els/
├── app.py                    # Main Flask application
├── requirements.txt          # Dependencies
├── Dockerfile                # Docker image
├── docker-compose.yml        # Docker compose config
├── users.db                  # SQLite database
├── templates/                # HTML templates
│   ├── register.html
│   ├── login.html
│   ├── dashboard.html
│   ├── forgot_password.html
│   └── reset_password.html
├── SETUP.md                  # Setup guide
├── DOCKER_DEPLOY.md          # Deployment guide
└── QUICKSTART.md             # Quick reference
```

## 🔐 Security Features

- Password hashing with Werkzeug
- CSRF protection
- SQL injection prevention
- Secure password reset tokens
- Input validation
- Login required decorator

## 🐳 Docker

```bash
docker-compose up
```

## ☁️ Deployment

**DigitalOcean (Recommended):**
1. Go to https://cloud.digitalocean.com
2. Create App from GitHub repo
3. Select Dockerfile
4. Add environment variables
5. Deploy!

See [DOCKER_DEPLOY.md](DOCKER_DEPLOY.md) for more options.

## 📚 Routes

- `/register` - Registration
- `/login` - Login
- `/dashboard` - Protected dashboard
- `/logout` - Logout
- `/forgot-password` - Password reset request
- `/reset-password/<token>` - Password reset

## 📖 Documentation

- [SETUP.md](SETUP.md) - Local setup
- [DOCKER_DEPLOY.md](DOCKER_DEPLOY.md) - Deployment
- [QUICKSTART.md](QUICKSTART.md) - Quick start

---

**Built with Flask + Docker**" 
