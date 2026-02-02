# Railway Deployment - Step by Step Guide

## ✅ Step 1: Git Repository Ready
Your code is now committed and ready. Current status:
- ✅ Git initialized
- ✅ All files committed
- ⏭️ Next: Push to GitHub

## 📋 Step 2: Create GitHub Repository

### 2.1 Go to GitHub
1. Visit https://github.com/new
2. Sign in (create account if needed)

### 2.2 Create New Repository
- **Repository name**: `hostel-hms` (or any name you prefer)
- **Description**: "Hostel Management System - HMS"
- **Visibility**: Public (Railway needs to access it)
- **DO NOT** initialize with README or .gitignore (we already have these)
- Click **"Create repository"**

### 2.3 You'll see commands like:
```
git remote add origin https://github.com/YOUR-USERNAME/hostel-hms.git
git branch -M main
git push -u origin main
```

## 🚀 Step 3: Push to GitHub

Copy and paste these commands in your terminal:

```powershell
cd 'c:\Users\aruni\Downloads\hostel_hms_copy\hostel_hms_copy'

# Add GitHub remote (replace YOUR-USERNAME)
git remote add origin https://github.com/YOUR-USERNAME/hostel-hms.git
git branch -M main
git push -u origin main
```

**Note**: Replace `YOUR-USERNAME` with your actual GitHub username!

After running, you'll see your code on GitHub at:
`https://github.com/YOUR-USERNAME/hostel-hms`

## 🎯 Step 4: Deploy on Railway

### 4.1 Go to Railway
1. Visit https://railway.app
2. Click **"Sign Up"** (or login if you have account)
3. Choose **"Continue with GitHub"** (easiest)

### 4.2 New Project
1. Click **"New Project"**
2. Select **"Deploy from GitHub repo"**
3. Railway will ask to authorize GitHub access - click **"Authorize"**

### 4.3 Select Your Repository
1. Find and select **`hostel-hms`** repository
2. Click **"Deploy Now"**

Railway will:
- Auto-detect Django
- Create necessary services
- Start building (takes 1-2 minutes)

### 4.4 Wait for Build Complete
You'll see logs showing:
```
✓ Building Docker image
✓ Building image complete
✓ Deploying...
✓ Deployment successful
```

## ⚙️ Step 5: Configure Environment Variables

### 5.1 In Railway Dashboard
1. Go to your project → **"Variables"** tab
2. Add these variables:

| Key | Value | How to Get |
|-----|-------|-----------|
| `SECRET_KEY` | Generate random key | Run: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"` |
| `DEBUG` | `False` | Production mode |
| `ALLOWED_HOSTS` | `*.railway.app` | Allows Railway domain |
| `EMAIL_HOST_USER` | your-email@gmail.com | Your Gmail address |
| `EMAIL_HOST_PASSWORD` | app-specific-password | [Generate here](https://myaccount.google.com/apppasswords) |

### 5.2 Generate SECRET_KEY Locally
```powershell
cd 'c:\Users\aruni\Downloads\hostel_hms_copy\hostel_hms_copy'
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copy the output and paste in Railway Variables

### 5.3 Email Setup (Optional but Recommended)
1. Enable 2FA on Gmail: https://myaccount.google.com/security
2. Generate App Password: https://myaccount.google.com/apppasswords
3. Use that password (not your real Gmail password!)

## 💾 Step 6: Add PostgreSQL Database

### 6.1 In Railway Dashboard
1. Go to your project
2. Click **"+ Add"** button
3. Select **"Add Service"** → **"PostgreSQL"**
4. Railway automatically creates `DATABASE_URL` variable

### 6.2 Verify Connection
- Railway will show "✓ Ready" when PostgreSQL is deployed
- Database URL is automatically in variables

## 🌐 Your Live URL

After all steps complete, your app will be live at:
```
https://[project-name].railway.app
```

Example: `https://hostel-hms-production.railway.app`

You can find the exact URL in Railway dashboard → **"Deployments"** tab

## ✨ Features Included

✅ Django 5.2.9  
✅ PostgreSQL Database  
✅ Static files served via WhiteNoise  
✅ Email configuration  
✅ SSL/TLS (auto-enabled)  
✅ Auto-scaling  
✅ Free monitoring & logs  

## 📝 Quick Troubleshooting

| Problem | Solution |
|---------|----------|
| Build fails | Check Railway logs (Deployments tab) |
| Static files not loading | Already fixed with WhiteNoise ✓ |
| Database errors | Check PostgreSQL is deployed and DATABASE_URL is set |
| Email not working | Verify app password is correct, not Gmail password |
| 500 errors | Check logs with `railway logs` command |

## 🔄 Auto-Deploy Future Changes

After initial setup, every push to GitHub auto-deploys:

```powershell
# Make changes locally
git add .
git commit -m "Update landing page colors"
git push origin main

# Changes live in ~2 minutes! 🚀
```

## 📚 Useful Railway Commands

```powershell
# View logs in real-time
railway logs

# View environment variables
railway variables

# Check deployment status
railway deployment
```

---

**Ready?** Follow steps 2-6 above to deploy! 🎉
