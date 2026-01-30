# Registration System Setup Guide

## Features
✅ **User Registration** - Simple registration with username, email, and password
✅ **User Login** - Secure login with session management
✅ **Password Reset** - Secure password recovery via email
✅ **Dashboard** - Protected user dashboard

## Environment Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Email (Optional - for Password Reset)

#### Gmail Setup:
1. Enable 2-Factor Authentication on your Gmail account
2. Generate an App Password:
   - Go to myaccount.google.com
   - Navigate to Security > App passwords
   - Select "Mail" and "Windows Computer"
   - Copy the generated 16-character password

#### Set Environment Variables:
Create a `.env` file in the project root:
```
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-16-char-app-password
MAIL_DEFAULT_SENDER=noreply@registration.com
```

Or set them in your terminal:
```bash
export MAIL_SERVER=smtp.gmail.com
export MAIL_PORT=587
export MAIL_USE_TLS=True
export MAIL_USERNAME=your-email@gmail.com
export MAIL_PASSWORD=your-app-password
export MAIL_DEFAULT_SENDER=noreply@registration.com
```

### 3. Run the Application
```bash
python app.py
```
The app will be available at `http://localhost:5000`

## User Registration Flow

1. User registers with username, email, and password
2. User is immediately able to login
3. User is redirected to dashboard after successful login

## Password Recovery Flow

1. User clicks "Forgot your password?" on login page
2. Enters their email address
3. Receives a password reset email (valid for 1 hour)
4. Clicks reset link and enters new password
5. Can login with new password

## Database Schema

The SQLite database includes:
- `id` - User ID
- `username` - Unique username
- `email` - Unique email address
- `password` - Hashed password
- `reset_token` - Password reset token
- `reset_token_expires` - Reset token expiration time
- `created_at` - Account creation timestamp

## Security Features

✓ Password hashing with Werkzeug
✓ Secure token generation using secrets
✓ Token expiration (1h for password reset)
✓ Database constraints for unique usernames and emails
✓ Session management with login_required decorator

## Routes

- `GET/POST /register` - User registration
- `GET/POST /login` - User login
- `GET/POST /forgot-password` - Request password reset
- `GET/POST /reset-password/<token>` - Reset password with token
- `GET /dashboard` - Protected dashboard
- `GET /logout` - Logout user

## Troubleshooting

**Email not sending (Password Reset):**
- Check MAIL_USERNAME and MAIL_PASSWORD in .env
- Ensure Gmail App Password is set (not regular password)
- Check internet connection
- Review app.py error logs

**Cannot reset password:**
- Reset link may have expired (1 hour limit)
- Token not found in database
- Check reset_token and reset_token_expires values

