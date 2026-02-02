# Render Deployment Guide

## 🚀 3-Step Render Deployment

### Step 1: Go to Render
1. Visit https://render.com
2. Click **"Sign Up"**
3. Choose **"GitHub"** → Authorize

### Step 2: Create New Web Service
1. Click **"New +"** → **"Web Service"**
2. Select **"Hostel-Resident-Management-System"** from your repos
3. Fill in:
   - **Name**: `hostel-hms` (or any name)
   - **Runtime**: Python 3
   - **Region**: Oregon (or closest to you)
   - **Branch**: `main`
   - **Build Command**: Leave as is (auto-detected)
   - **Start Command**: `gunicorn hostel_hms.wsgi:application`

4. Click **"Create Web Service"**

Render will start deploying automatically! ✓

### Step 3: Add Environment Variables

Once deployment completes (you'll see ✓):

1. Go to your service → **"Environment"** tab
2. Add these variables:

| Key | Value |
|-----|-------|
| `SECRET_KEY` | Generate: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"` |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `*.onrender.com` |
| `EMAIL_HOST_USER` | your-email@gmail.com |
| `EMAIL_HOST_PASSWORD` | Gmail app password |

3. Click **"Save"** → Render auto-redeploys ✓

### Step 4: Add PostgreSQL Database (Optional)

1. Click **"New +"** → **"PostgreSQL"**
2. Fill in name: `hostel-db`
3. Click **"Create"**
4. Copy the **Internal Database URL**
5. Go back to your Web Service → **"Environment"**
6. Add variable:
   - **Key**: `DATABASE_URL`
   - **Value**: Paste the URL from PostgreSQL

7. Click **"Save"**

---

## ✨ Your Live App

Once deployed, you'll get a URL like:
```
https://hostel-hms.onrender.com
```

---

## 📋 Quick Checklist

- ✅ Code on GitHub
- ✅ render.yaml config created
- ⏭️ Connect Render to GitHub
- ⏭️ Add environment variables
- ⏭️ Live! 🎉

---

## 🔄 Auto-Deploy

Push to GitHub and Render auto-deploys:
```powershell
git add .
git commit -m "Your changes"
git push origin main
# Live in ~2 minutes!
```

---

**Ready? Go to https://render.com and follow Step 1!**
