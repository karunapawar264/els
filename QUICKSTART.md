# 🚀 Quick Deployment Guide

Your Flask registration system is ready to deploy! Here are the quickest options:

## 1️⃣ Deploy to Render (Recommended - Easiest)

**Time: ~5 minutes**

1. Go to https://render.com
2. Sign up (free)
3. Click **New +** → **Web Service**
4. Connect your GitHub repo: `karunapawar264/els`
5. Configure:
   - **Name:** els-registration
   - **Runtime:** Python 3
   - **Build:** `pip install -r requirements.txt`
   - **Start:** `gunicorn app:app`
   - **Region:** Choose closest to you
6. **Environment Variables:** (Copy from `.env.example`)
   ```
   MAIL_SERVER=smtp.gmail.com
   MAIL_PORT=587
   MAIL_USE_TLS=True
   MAIL_USERNAME=your-email@gmail.com
   MAIL_PASSWORD=your-app-password
   MAIL_DEFAULT_SENDER=noreply@registration.com
   ```
7. Click **Create Web Service**
8. Done! Your app will deploy in ~2 minutes

**Your URL:** `https://els-registration.onrender.com`

---

## 2️⃣ Deploy to Heroku (Still Works)

```bash
heroku login
heroku create your-app-name
git push heroku main
heroku config:set MAIL_SERVER=smtp.gmail.com
# ... set other env vars ...
```

---

## 3️⃣ Deploy with Docker (DigitalOcean, AWS)

```bash
docker build -t els-registration .
docker run -p 5000:5000 els-registration
```

---

## ⚙️ Getting Gmail App Password

Your emails won't send without this:

1. Go to https://myaccount.google.com/security
2. Enable **2-Step Verification** (if not enabled)
3. Scroll to **App passwords**
4. Select **Mail** → **Windows Computer**
5. Copy the 16-character password
6. Use it as `MAIL_PASSWORD` in env variables

---

## ✅ After Deployment

Test your live app:
- Register a new user
- Try to login
- Test password reset
- Check email receives reset link

---

## 📋 What's Deployed

✅ User Registration
✅ User Login  
✅ Password Reset
✅ Protected Dashboard
✅ Session Management
✅ Password Hashing

---

## 🔗 Quick Links

- **GitHub:** https://github.com/karunapawar264/els
- **Render:** https://render.com
- **Heroku:** https://heroku.com
- **DigitalOcean:** https://digitalocean.com

---

Need help? See [DEPLOY.md](DEPLOY.md) for detailed instructions.
