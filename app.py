from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mail import Mail, Message
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import os
import secrets
from datetime import datetime, timedelta
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-in-production'

# Email Configuration
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 587))
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', True)
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME', 'your-email@gmail.com')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD', 'your-app-password')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER', 'noreply@registration.com')

mail = Mail(app)

# Database setup
DATABASE = 'users.db'

def init_db():
    if not os.path.exists(DATABASE):
        conn = sqlite3.connect(DATABASE, timeout=10.0)
        conn.execute('PRAGMA journal_mode=WAL')  # Enable Write-Ahead Logging
        c = conn.cursor()
        c.execute('''CREATE TABLE users
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      username TEXT UNIQUE NOT NULL,
                      email TEXT UNIQUE NOT NULL,
                      password TEXT NOT NULL,
                      reset_token TEXT,
                      reset_token_expires TIMESTAMP,
                      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
        conn.commit()
        conn.close()
    else:
        # Add columns if they don't exist (for existing databases)
        conn = sqlite3.connect(DATABASE, timeout=10.0)
        conn.execute('PRAGMA journal_mode=WAL')  # Enable Write-Ahead Logging
        c = conn.cursor()
        try:
            c.execute('ALTER TABLE users ADD COLUMN reset_token TEXT')
            c.execute('ALTER TABLE users ADD COLUMN reset_token_expires TIMESTAMP')
            c.execute('ALTER TABLE users ADD COLUMN created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP')
            conn.commit()
        except sqlite3.OperationalError:
            pass  # Columns already exist
        conn.close()

def get_db():
    conn = sqlite3.connect(DATABASE, timeout=10.0)
    conn.row_factory = sqlite3.Row
    conn.execute('PRAGMA journal_mode=WAL')  # Write-Ahead Logging for better concurrency
    return conn

def send_reset_password_email(email, username, token):
    try:
        reset_url = url_for('reset_password', token=token, _external=True)
        msg = Message('Password Reset Request',
                      recipients=[email],
                      html=f'''
                      <h2>Password Reset Request</h2>
                      <p>Hi {username},</p>
                      <p>We received a request to reset your password. Click the link below:</p>
                      <p><a href="{reset_url}" style="background-color: #667eea; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; display: inline-block;">Reset Password</a></p>
                      <p>Or copy this link: {reset_url}</p>
                      <p>This link expires in 1 hour.</p>
                      <p>If you didn't request this, please ignore this email.</p>
                      ''')
        mail.send(msg)
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('register'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    success = None
    if request.method == 'POST':
        username = request.form.get('username').strip() if request.form.get('username') else None
        email = request.form.get('email').strip() if request.form.get('email') else None
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        # Validation
        if not username or not email or not password or not confirm_password:
            error = 'All fields are required'
        elif len(username) < 3:
            error = 'Username must be at least 3 characters'
        elif len(password) < 6:
            error = 'Password must be at least 6 characters long'
        elif password != confirm_password:
            error = 'Passwords do not match'
        elif '@' not in email:
            error = 'Please enter a valid email address'
        else:
            try:
                conn = get_db()
                c = conn.cursor()
                
                # Hash password using Werkzeug's built-in PBKDF2 with scrypt
                hashed_password = generate_password_hash(password)
                
                # Insert new user into database
                c.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)',
                         (username, email, hashed_password))
                conn.commit()
                
                # Log successful user creation
                print(f"✅ New user registered: {username} ({email})")
                print(f"   Password hash: {hashed_password[:50]}...")
                
                conn.close()
                success = f'Account created successfully! Please login with your credentials.'
                # Redirect to login after 2 seconds
                return render_template('register.html', success=success, redirect_to='login')
                
            except sqlite3.IntegrityError as e:
                if 'username' in str(e):
                    error = f'Username "{username}" is already taken'
                elif 'email' in str(e):
                    error = f'Email "{email}" is already registered'
                else:
                    error = 'Registration failed. Please try again.'
            except Exception as e:
                print(f"❌ Registration error: {e}")
                error = f'An error occurred during registration. Please try again.'
    
    return render_template('register.html', error=error, success=success)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            error = 'Username and password are required'
        else:
            conn = get_db()
            c = conn.cursor()
            c.execute('SELECT * FROM users WHERE username = ?', (username,))
            user = c.fetchone()
            conn.close()

            if user and check_password_hash(user['password'], password):
                session['username'] = user['username']
                session['email'] = user['email']
                session['user_id'] = user['id']
                return redirect(url_for('dashboard'))
            else:
                error = 'Invalid username or password'
    
    return render_template('login.html', error=error)

@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    error = None
    if request.method == 'POST':
        email = request.form.get('email')
        
        if not email:
            error = 'Email is required'
        else:
            conn = get_db()
            c = conn.cursor()
            c.execute('SELECT * FROM users WHERE email = ?', (email,))
            user = c.fetchone()
            
            if user:
                reset_token = secrets.token_urlsafe(32)
                expires = datetime.now() + timedelta(hours=1)
                
                c.execute('UPDATE users SET reset_token = ?, reset_token_expires = ? WHERE id = ?',
                         (reset_token, expires, user['id']))
                conn.commit()
                
                send_reset_password_email(email, user['username'], reset_token)
            
            conn.close()
            # Always show success message for security (don't reveal if email exists)
            return render_template('reset_pending.html', email=email)
    
    return render_template('forgot_password.html', error=error)

@app.route('/reset-password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    conn = get_db()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE reset_token = ?', (token,))
    user = c.fetchone()
    
    if not user or (user['reset_token_expires'] and datetime.fromisoformat(user['reset_token_expires']) < datetime.now()):
        error = 'Invalid or expired reset link'
        return render_template('reset_result.html', success=False, message=error)
    
    error = None
    if request.method == 'POST':
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        if not password or not confirm_password:
            error = 'All fields are required'
        elif password != confirm_password:
            error = 'Passwords do not match'
        elif len(password) < 6:
            error = 'Password must be at least 6 characters long'
        else:
            hashed_password = generate_password_hash(password)
            c.execute('UPDATE users SET password = ?, reset_token = NULL, reset_token_expires = NULL WHERE id = ?',
                     (hashed_password, user['id']))
            conn.commit()
            conn.close()
            
            message = 'Password reset successfully! You can now login with your new password.'
            return render_template('reset_result.html', success=True, message=message)
    
    conn.close()
    return render_template('reset_password.html', token=token, error=error)

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', username=session['username'])

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)
