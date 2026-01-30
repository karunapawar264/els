# Docker Deployment Guide

## Local Testing with Docker

### 1. Build the Docker Image:
```bash
cd /workspaces/els
docker build -t els-registration .
```

### 2. Run with Docker Compose (Easiest):

Create a `.env` file with your email credentials:
```bash
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
MAIL_DEFAULT_SENDER=noreply@registration.com
```

Then run:
```bash
docker-compose up
```

Visit: http://localhost:5000

Stop with: `docker-compose down`

### 3. Run with Docker Directly:
```bash
docker run -p 5000:5000 \
  -e MAIL_USERNAME=your-email@gmail.com \
  -e MAIL_PASSWORD=your-app-password \
  -e MAIL_DEFAULT_SENDER=noreply@registration.com \
  els-registration
```

---

## Deploy to Cloud Platforms

### Option 1: DigitalOcean App Platform (Recommended)

**Time: ~10 minutes**

1. **Push code to GitHub** (already done)

2. **Go to DigitalOcean:**
   - Log in to https://cloud.digitalocean.com
   - Click **Create** → **App**

3. **Configure:**
   - Select your GitHub repo: `karunapawar264/els`
   - Choose Dockerfile
   - Set **Port:** 5000
   - Set **HTTP Port:** 5000

4. **Environment Variables:**
   ```
   MAIL_USERNAME=your-email@gmail.com
   MAIL_PASSWORD=your-app-password
   MAIL_DEFAULT_SENDER=noreply@registration.com
   FLASK_ENV=production
   ```

5. **Deploy** → Wait 5-10 minutes

**Your URL:** `https://els-registration-xxx.ondigitalocean.app`

---

### Option 2: AWS ECS (More Control)

```bash
# 1. Create ECR repository
aws ecr create-repository --repository-name els-registration --region us-east-1

# 2. Get login token
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin YOUR_ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com

# 3. Build and push
docker build -t els-registration .
docker tag els-registration:latest YOUR_ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/els-registration:latest
docker push YOUR_ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/els-registration:latest

# 4. Create ECS task definition and service in AWS Console
```

---

### Option 3: Google Cloud Run (Serverless)

```bash
# 1. Authenticate
gcloud auth login

# 2. Set project
gcloud config set project YOUR_PROJECT_ID

# 3. Deploy directly from GitHub
gcloud run deploy els-registration \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars MAIL_USERNAME=your-email@gmail.com,MAIL_PASSWORD=your-app-password
```

---

### Option 4: Heroku with Docker

```bash
# 1. Create heroku.yml
cat > heroku.yml << EOF
build:
  docker:
    web: Dockerfile
run:
  web: gunicorn app:app
EOF

# 2. Push
git add heroku.yml
git commit -m "Add heroku.yml"
git push heroku main

# 3. Set environment variables
heroku config:set MAIL_USERNAME=your-email@gmail.com
heroku config:set MAIL_PASSWORD=your-app-password
```

---

### Option 5: Self-Hosted on VPS (Linode, Vultr, AWS EC2)

```bash
# 1. SSH into your server
ssh root@your-server-ip

# 2. Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# 3. Clone repository
git clone https://github.com/karunapawar264/els.git
cd els

# 4. Create .env file
nano .env
# Add your email credentials

# 5. Run with docker-compose
docker-compose up -d

# 6. Setup Nginx reverse proxy (optional)
sudo apt install nginx
# Configure nginx to proxy to localhost:5000
```

---

## Recommended: DigitalOcean App Platform

**Why?**
- ✅ Easiest setup (connect GitHub, click deploy)
- ✅ Auto deploys on push to main
- ✅ Free SSL/HTTPS
- ✅ Good performance
- ✅ $5-12/month

**Steps:**
1. Go to https://cloud.digitalocean.com
2. Click **Apps** → **Create App**
3. Select your GitHub repo
4. Choose Dockerfile
5. Add environment variables
6. Deploy!

---

## Monitoring & Logs

**DigitalOcean:**
```bash
doctl apps logs YOUR_APP_ID
```

**Google Cloud Run:**
```bash
gcloud run logs read els-registration --limit 50
```

**AWS ECS:**
- CloudWatch Logs

---

## Cost Estimates

| Platform | Cost | Notes |
|----------|------|-------|
| DigitalOcean App | $5-12/mo | Easiest, recommended |
| AWS ECS | $0-50/mo | Pay per usage |
| Google Cloud Run | $0-50/mo | Free tier available |
| Heroku | $7-50/mo | Simple setup |
| VPS (Linode) | $5-50/mo | Full control |

