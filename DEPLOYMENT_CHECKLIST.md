# MetroMind AI - Deployment Checklist

## Pre-Deployment Verification

### Code Quality
- [ ] All imports resolved
- [ ] No syntax errors
- [ ] No commented debug code
- [ ] Proper error handling
- [ ] Functions documented

### Database
- [ ] Database schema created
- [ ] Tables initialized
- [ ] Indexes added for performance
- [ ] Backup strategy planned

### Email Configuration
- [ ] Gmail 2FA enabled
- [ ] App password generated (16 chars)
- [ ] .env file configured (DO NOT COMMIT)
- [ ] Test email sent successfully

### SMS Configuration (Optional)
- [ ] Choose provider (Twilio/Africa's Talking)
- [ ] Account created with free credits
- [ ] Credentials obtained
- [ ] .env configured
- [ ] Test SMS sent

### API Security
- [ ] Admin token changed from default
- [ ] CORS properly configured for Vercel URL
- [ ] Input validation on all endpoints
- [ ] Error messages don't expose internals
- [ ] Rate limiting implemented

---

## PythonAnywhere Deployment

### Step 1: Prepare Backend

```bash
# 1. Clone/upload to PythonAnywhere
git clone <your-repo> metromind
# OR upload files via web

# 2. Setup virtual environment
python3.9 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r backend/requirements.txt

# 4. Create .env in backend directory
nano backend/.env
# Add all configuration

# 5. Test locally
python backend/main.py
# Visit http://127.0.0.1:5000
```

### Step 2: Configure Web App

1. **PythonAnywhere Dashboard → Web**
2. **Create new web app → Flask**
3. **Configuration:**
   - Source code: `/home/username/metromind/backend`
   - Working directory: `/home/username/metromind/backend`
   - Python version: 3.9

4. **WSGI file** (`/home/username/metromind.com_wsgi.py`):
```python
import sys
import os

path = os.path.expanduser('~/metromind/backend')
if path not in sys.path:
    sys.path.insert(0, path)

from main import app as application

# Fix CORS for production
from flask_cors import CORS
CORS(application, resources={r"/api/*": {"origins": ["your-vercel-url.vercel.app"]}})
```

5. **Source code → setup_files.py**
```python
import os
os.chdir('/home/username/metromind/backend')
from models import init_db, init_transit_capacity
init_db()
init_transit_capacity()
```

6. **Web tab → Add environment variable**
   - PYTHONPATH: `/home/username/metromind/backend`

7. **Reload web app**

### Step 3: Verify

```bash
# Test API endpoints
curl https://yourusername.pythonanywhere.com/api/health

# Should return:
# {"status": "healthy", "service": "MetroMind Trip Planner", "version": "2.0"}
```

---

## Vercel Deployment

### Step 1: Prepare Frontend

```bash
# 1. In frontend directory
cd frontend

# 2. Create .env.production
REACT_APP_API_URL=https://yourusername.pythonanywhere.com

# 3. Build
npm run build

# 4. Test build locally
npm install -g serve
serve -s build
# Visit http://localhost:3000
```

### Step 2: Deploy to Vercel

```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
cd frontend
vercel

# Answers:
# - Project name: metromind-frontend
# - Which scope: your-username
# - Link to existing project: No
# - Build command: npm run build (default)
# - Output directory: build (default)
```

### Step 3: Configure Environment

1. **Vercel Dashboard → Settings → Environment Variables**
2. **Add:**
   - Name: `REACT_APP_API_URL`
   - Value: `https://yourusername.pythonanywhere.com`
   - Environment: Production

3. **Redeploy for changes to take effect**

### Step 4: Custom Domain (Optional)

1. **Vercel Dashboard → Settings → Domains**
2. **Add your domain**
3. **Follow DNS instructions**

---

## Post-Deployment Testing

### Frontend Verification
- [ ] Visit Vercel URL
- [ ] UI loads correctly
- [ ] All images load
- [ ] No console errors
- [ ] Auth modal appears
- [ ] Can login

### Backend Verification
- [ ] Health endpoint responds
- [ ] GET /api/locations works
- [ ] GET /api/bus-routes works
- [ ] POST /api/auth/signup works
- [ ] Admin endpoints require token

### Integration Testing
- [ ] Frontend connects to backend
- [ ] Signup creates user
- [ ] Login returns token
- [ ] Can book trip
- [ ] Email sent
- [ ] Admin dashboard loads

### Production Monitoring
- [ ] Monitor error logs
- [ ] Check database size
- [ ] Verify backups running
- [ ] Monitor API response times
- [ ] Check email delivery rate
- [ ] Monitor SMS costs (if applicable)

---

## Common Issues & Solutions

### Issue: CORS Error
**Solution:**
```python
# In main.py
from flask_cors import CORS
CORS(app, 
    origins=['https://your-vercel-url.vercel.app'],
    supports_credentials=True
)
```

### Issue: Static files not loading
**Solution:**
- Vercel builds static files automatically
- Ensure `npm run build` works locally
- Check build directory in package.json

### Issue: Email not working
**Solution:**
```bash
# Test connection
telnet smtp.gmail.com 465
# Should connect

# Verify credentials
python -c "from notifications import send_order_confirmation_email; print('OK')"
```

### Issue: Database locked
**Solution:**
```bash
# SSH into PythonAnywhere
rm /home/username/metromind/backend/metromind.db
# Restart web app - DB will recreate
```

### Issue: API timeout
**Solution:**
- Increase PythonAnywhere timeout (Web tab → Max request time)
- Check for long-running queries
- Optimize database indexes

---

## Backup & Maintenance

### Weekly Tasks
- [ ] Backup database
- [ ] Check error logs
- [ ] Verify email delivery
- [ ] Monitor SMS balance

### Monthly Tasks
- [ ] Review admin logs
- [ ] Check user statistics
- [ ] Test email templates
- [ ] Test SMS delivery

### Quarterly Tasks
- [ ] Update dependencies
- [ ] Security audit
- [ ] Performance review
- [ ] Cost optimization

---

## Database Backup

### PythonAnywhere
```bash
# Connect via SSH
# Backup SQLite
cp /home/username/metromind/backend/metromind.db \
   /home/username/backups/metromind_$(date +%Y%m%d).db

# Schedule daily with cron
crontab -e
# Add: 0 2 * * * cp /home/username/metromind/backend/metromind.db /home/username/backups/metromind_$(date +\%Y\%m\%d).db
```

---

## Rollback Plan

### If Deployment Fails

1. **Frontend**
   ```bash
   # Revert to previous Vercel deployment
   Vercel Dashboard → Deployments → Click previous → Redeploy
   ```

2. **Backend**
   ```bash
   # Revert code
   git revert HEAD
   git push
   
   # Reload web app on PythonAnywhere
   ```

---

## Monitoring URLs

### Health Endpoints
```
Production API: https://yourusername.pythonanywhere.com/api/health
Production Frontend: https://your-domain.vercel.app
```

### Admin Dashboard
```
https://your-domain.vercel.app/admin
Token: admin_secret (CHANGE IN PRODUCTION)
```

---

## Security Checklist

Before going live:
- [ ] Change admin token from default
- [ ] Enable HTTPS everywhere
- [ ] Update CORS origins
- [ ] Remove debug endpoints
- [ ] Implement rate limiting
- [ ] Enable database authentication
- [ ] Set secure cookie flags
- [ ] Implement API key rotation
- [ ] Setup monitoring alerts
- [ ] Create incident response plan

---

## Support & Troubleshooting

### PythonAnywhere Support
- Dashboard → Help & Support
- Email: support@pythonanywhere.com

### Vercel Support
- Dashboard → Help
- Support portal: https://vercel.com/support

### Email Issues
- Gmail: https://support.google.com/accounts
- Twilio: https://www.twilio.com/docs/usage/api

---

## Go-Live Checklist

Final verification before production:
- [ ] All tests passing
- [ ] No critical errors in logs
- [ ] Performance acceptable
- [ ] Backups configured
- [ ] Monitoring active
- [ ] Team trained
- [ ] Documentation updated
- [ ] Incident plan ready
- [ ] Marketing/announcement ready
- [ ] Analytics configured

---

**Deployment Date: _______________**
**Deployed By: _______________**
**Status: [ ] Development [ ] Testing [ ] Production**

Last updated: June 2024
