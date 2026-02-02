# Railway Deployment Guide

## Quick Start

Your Hostel Management System is now ready for deployment on Railway! Follow these steps:

### Step 1: Initialize Git Repository

```powershell
cd c:\Users\aruni\Downloads\hostel_hms_copy\hostel_hms_copy
git init
git add .
git commit -m "Initial commit: HMS deployment ready"
git branch -M main
```

### Step 2: Create GitHub Repository

1. Go to https://github.com/new
2. Create a new repository (name: `hostel-hms` or similar)
3. Copy the repository URL

### Step 3: Push to GitHub

```powershell
git remote add origin https://github.com/YOUR-USERNAME/hostel-hms.git
git push -u origin main
```

### Step 4: Deploy on Railway

1. **Go to Railway**: https://railway.app
2. **Sign up** (free tier available)
3. **Click "New Project"**
4. **Select "Deploy from GitHub repo"**
5. **Authorize Railway** to access your GitHub account
6. **Select your `hostel-hms` repository**
7. Railway will auto-detect Django and set up services

### Step 5: Configure Environment Variables

Once Railway detects your project:

1. Go to your project → **Variables**
2. Add these environment variables:

```
SECRET_KEY=your-very-secure-random-key-change-this
DEBUG=False
ALLOWED_HOSTS=*.railway.app
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-gmail-app-password
```

**Generate SECRET_KEY**:
```powershell
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Step 6: Add PostgreSQL Database

1. In Railway project → **Create** → **Add PostgreSQL**
2. Railway will automatically link it and create `DATABASE_URL`
3. No additional configuration needed!

### Step 7: Deploy

- Click **"Deploy"**
- Wait for build to complete (~2-3 minutes)
- Your app will be live at: `https://your-project-name.railway.app`

## What Gets Deployed

✅ Full Django application  
✅ PostgreSQL database  
✅ Static files (CSS, JS, images)  
✅ Media files (if any)  
✅ Email configuration  

## Database Migrations

Migrations run automatically on deploy via `Procfile`:
```
web: python manage.py migrate && gunicorn hostel_hms.wsgi
```

## Auto-Deploy on Git Push

After initial setup, every push to `main` branch automatically deploys:

```powershell
git add .
git commit -m "Update landing page"
git push origin main
# Your changes will be live in ~2 minutes!
```

## Production URLs

After deployment:
- **Main app**: `https://your-project-name.railway.app`
- **Admin panel**: `https://your-project-name.railway.app/admin`

## Email Configuration (Gmail)

1. Enable 2-Step Verification on your Gmail account
2. Generate [App Password](https://myaccount.google.com/apppasswords)
3. Use the app password in `EMAIL_HOST_PASSWORD` variable

## Troubleshooting

### Build fails?
- Check Railway logs: Project → Deployments → View logs
- Ensure all imports work: `python manage.py check`

### Static files not loading?
- Already handled by WhiteNoise middleware ✅
- Configured in `settings.py` ✅

### Database errors?
- Migrations run automatically ✅
- Check Railway PostgreSQL connection in Variables

### Email not working?
- Verify Gmail app password is correct
- Check Railway logs for email errors

## Monitoring

In Railway dashboard:
- **Logs** → View real-time application logs
- **Metrics** → Monitor CPU, memory, requests
- **Settings** → Manage variables and services

## Costs

Railway free tier includes:
- 5GB storage
- $5/month credit (plenty for hobby projects)
- Free PostgreSQL database
- SSL certificate included

## Next Steps

1. ✅ Landing page improved (DONE)
2. 📝 Initialize Git repository
3. 🔗 Push to GitHub
4. 🚀 Deploy on Railway
5. 🎉 Live!

---

**Questions?** Check Railway docs: https://docs.railway.app
