# Production Deployment Checklist

Before deploying to production, complete these steps:

## Security

- [ ] Change Flask `secret_key` in app.py to a strong random string
  ```python
  app.secret_key = 'your-super-secret-random-string-here'
  ```
- [ ] Set `FLASK_ENV=production` in environment variables
- [ ] Enable HTTPS/SSL (automatic with cloud platforms)
- [ ] Review security headers
- [ ] Enable CORS if needed
- [ ] Rate limit login attempts

## Database

- [ ] Migrate from SQLite to PostgreSQL
- [ ] Set up database backups (daily or more frequent)
- [ ] Test database recovery procedure
- [ ] Use strong database passwords
- [ ] Enable database encryption

## Email

- [ ] Configure Gmail App Password or SMTP provider
- [ ] Test email sending (register → password reset flow)
- [ ] Set valid `MAIL_DEFAULT_SENDER` email
- [ ] Monitor failed email deliveries
- [ ] Set up bounce handling

## Deployment

- [ ] Push all code to GitHub
- [ ] Review all environment variables
- [ ] Set up monitoring/logging
- [ ] Configure error tracking (Sentry, etc.)
- [ ] Enable automatic deployments (CI/CD)
- [ ] Test deployment process
- [ ] Set up rollback procedure

## Performance

- [ ] Enable database query caching
- [ ] Set up content delivery network (CDN)
- [ ] Optimize images and static files
- [ ] Enable gzip compression
- [ ] Monitor response times
- [ ] Set up performance alerts

## Backup & Recovery

- [ ] Automated daily database backups
- [ ] Test backup restoration
- [ ] Document recovery procedures
- [ ] Keep encrypted backups off-site
- [ ] Document disaster recovery plan

## Monitoring

- [ ] Set up server monitoring (CPU, memory, disk)
- [ ] Monitor error logs
- [ ] Set up uptime monitoring
- [ ] Configure alerts for critical issues
- [ ] Track user registration metrics
- [ ] Monitor email delivery rates

## Domain & DNS

- [ ] Purchase domain name
- [ ] Configure DNS records
- [ ] Set up email DNS (SPF, DKIM, DMARC)
- [ ] Configure SSL certificate (usually automatic)
- [ ] Set up subdomain for API (if needed)

## Testing

- [ ] Test registration flow end-to-end
- [ ] Test login flow
- [ ] Test password reset flow
- [ ] Test with multiple browsers
- [ ] Test on mobile devices
- [ ] Load testing (simulate users)
- [ ] Security testing

## Documentation

- [ ] Document deployment process
- [ ] Document emergency procedures
- [ ] Create runbooks for common issues
- [ ] Document API endpoints
- [ ] Create user guide

## Compliance

- [ ] Review privacy policy
- [ ] Implement GDPR compliance (if EU users)
- [ ] Set up cookie consent
- [ ] Document data retention policy
- [ ] Enable audit logging

## Post-Deployment

- [ ] Monitor error logs daily
- [ ] Check database size
- [ ] Review user feedback
- [ ] Plan scaling strategy
- [ ] Schedule security updates
- [ ] Plan feature improvements

## Quick Deployment Summary

### Option 1: DigitalOcean (Recommended)
```bash
# 1. Push to GitHub (already done)
git push origin main

# 2. Go to https://cloud.digitalocean.com
# 3. Create App from repo
# 4. Select Dockerfile
# 5. Add environment variables
# 6. Deploy!
```

### Option 2: Self-Hosted VPS
```bash
# 1. SSH into server
ssh root@your-ip

# 2. Install Docker
curl -fsSL https://get.docker.com | sh

# 3. Clone repo
git clone https://github.com/karunapawar264/els.git

# 4. Create .env file
echo "MAIL_USERNAME=..." > .env

# 5. Run
docker-compose up -d

# 6. Set up Nginx reverse proxy (optional)
# 7. Configure SSL with Let's Encrypt
```

### Option 3: Cloud Run (Serverless)
```bash
gcloud run deploy els-registration \
  --source . \
  --platform managed \
  --region us-central1 \
  --set-env-vars MAIL_USERNAME=xxx,MAIL_PASSWORD=xxx
```

## Support & Troubleshooting

**App not starting?**
- Check logs: `docker-compose logs`
- Verify environment variables
- Check database connectivity

**Email not sending?**
- Test SMTP credentials
- Check Gmail 2FA and App Password
- Review email logs

**Database issues?**
- Check database connectivity
- Verify backup integrity
- Review database logs

**Performance issues?**
- Check database query performance
- Monitor server resources
- Enable caching

---

**Remember:** Always test in a staging environment before deploying to production!
