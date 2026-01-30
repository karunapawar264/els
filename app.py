from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Required for flashing messages and session

# Mock user database for demonstration
users = {
    "test@example.com": {"password": "password123", "name": "Test User"}
}

@app.route('/')
def index():
    if 'user' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        mobile_no = request.form.get('mobile_no')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if not username or not email or not mobile_no or not password or not confirm_password:
            flash('All fields are required!', 'danger')
        elif password != confirm_password:
            flash('Passwords do not match!', 'danger')
        elif email in users:
            flash('Email already registered!', 'danger')
        else:
            # Save user to mock database
            users[email] = {
                "password": password, 
                "username": username,
                "mobile_no": mobile_no
            }
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = users.get(email)
        if user and user['password'] == password:
            session['user'] = email
            session['username'] = user['username']
            session['mobile_no'] = user['mobile_no']
            flash(f'Welcome back, {user["username"]}!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password.', 'danger')

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        flash('Please login to access this page.', 'danger')
        return redirect(url_for('login'))
    return render_template('dashboard.html', 
                           username=session['username'], 
                           mobile_no=session['mobile_no'])

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
