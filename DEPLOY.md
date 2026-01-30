# Deploy Registration System

This guide shows how to deploy your Flask registration application to the cloud.

## Option 1: Deploy to Render (Recommended - Free Tier Available)

### Steps:
1. Push your code to GitHub:
```bash
cd /workspaces/els
git add .
git commit -m "Add registration system"
git push origin main
```

2. Go to [render.com](https://render.com) and sign up

3. Click "New +" → "Web Service"

4. Connect your GitHub repository

5. Configure the service:
   - **Name:** els-registration (or your preferred name)
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`

6. Add Environment Variables:
   ```
   MAIL_SERVER=smtp.gmail.com
   MAIL_PORT=587
   MAIL_USE_TLS=True
   MAIL_USERNAME=your-email@gmail.com
   MAIL_PASSWORD=your-app-password
   MAIL_DEFAULT_SENDER=noreply@registration.com
   ```

7. Click "Create Web Service"

Your app will be deployed in a few minutes!

---

## Option 2: Deploy to Heroku (Free tier discontinued, but still available)

### Steps:
1. Install Heroku CLI: https://devcenter.heroku.com/articles/heroku-cli

2. Login to Heroku:
```bash
heroku login
```

3. Create a Heroku app:
```bash
heroku create your-app-name
```

4. Add environment variables:
```bash
heroku config:set MAIL_SERVER=smtp.gmail.com
heroku config:set MAIL_PORT=587
heroku config:set MAIL_USE_TLS=True
heroku config:set MAIL_USERNAME=your-email@gmail.com
heroku config:set MAIL_PASSWORD=your-app-password
heroku config:set MAIL_DEFAULT_SENDER=noreply@registration.com
```

5. Deploy:
```bash
git push heroku main
```

---

## Option 3: Deploy using Docker (AWS, DigitalOcean, etc.)

### Build and run Docker image:
```bash
# Build
docker build -t els-registration .

# Run locally
docker run -p 5000:5000 \
  -e MAIL_SERVER=smtp.gmail.com \
  -e MAIL_USERNAME=your-email@gmail.com \
  -e MAIL_PASSWORD=your-app-password \
  els-registration
```

### Deploy to DigitalOcean App Platform:
1. Push code to GitHub
2. Go to DigitalOcean → App Platform
3. Connect your GitHub repository
4. Select Dockerfile
5. Add environment variables
6. Deploy

---

## Option 4: Deploy to PythonAnywhere (Simple & Beginner Friendly)

### Steps:
1. Go to [pythonanywhere.com](https://pythonanywhere.com) and sign up (free tier available)

2. Click "Web" in the top menu

3. Add a new web app:
   - Select "Flask"
   - Select "Python 3.10"

4. Clone your repository:
   - Go to "Bash" console
   - Run: `git clone https://github.com/your-username/els.git`

5. Create virtual environment:
```bash
mkvirtualenv --python=/usr/bin/python3.10 myenv
cd els
pip install -r requirements.txt
```

6. Configure WSGI file:
   - Edit the WSGI configuration file provided
   - Point it to your app.py

7. Set environment variables in Web app configuration

8. Reload the web app

---

## Important: Database Persistence

⚠️ **Note:** SQLite databases don't persist on most cloud platforms. For production:

1. **Use PostgreSQL** (recommended):
```bash
pip install psycopg2-binary SQLAlchemy
```

2. Update your app.py to use PostgreSQL instead of SQLite

3. Create a database on the cloud platform

---

## Getting Gmail App Password for Email

1. Go to [myaccount.google.com](https://myaccount.google.com)
2. Click "Security" in the left menu
3. Enable 2-Factor Authentication if not already enabled
4. Scroll down to "App passwords"
5. Select "Mail" and "Windows Computer"
6. Copy the 16-character password
7. Use this as MAIL_PASSWORD in your environment variables

---

## Test Your Deployment

Once deployed:
1. Visit your app URL (e.g., https://your-app-name.onrender.com)
2. Test registration
3. Test login
4. Test password reset (if email is configured)

---

## Troubleshooting

**App not starting?**
- Check the build logs
- Verify Procfile exists
- Ensure requirements.txt has gunicorn

**Email not sending?**
- Verify MAIL_USERNAME and MAIL_PASSWORD
- Check email environment variables
- Review app logs for SMTP errors

**Database not persisting?**
- Migrate to PostgreSQL or MySQL
- Use cloud database service

**Port issues?**
- Cloud platforms use dynamic ports
- Make sure app listens on the correct port
- Don't hardcode port 5000

