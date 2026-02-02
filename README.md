# Hostel Management System (HMS)

A comprehensive Django-based hostel management system for students, authorities, and watchmen.

## Features

- **Student Portal**: File complaints, manage leave requests, track in/out status
- **Authority Portal**: Manage residents, review and resolve complaints, approve leaves, generate reports
- **Watchman Portal**: Record student entry/exit with timestamps
- **Predictive Analytics**: Supply prediction and maintenance alerts
- **Professional Dashboard**: Real-time insights and status monitoring

## Tech Stack

- **Backend**: Django 5.2.9
- **Database**: SQLite (development) / PostgreSQL (production)
- **Server**: Gunicorn + WhiteNoise
- **Frontend**: HTML5, CSS3, Font Awesome

## Local Development

### Prerequisites

- Python 3.11+
- pip
- Virtual environment

### Setup

1. **Clone the repository**
```bash
git clone <repository-url>
cd hostel_hms_copy
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Create .env file**
```bash
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

5. **Run migrations**
```bash
python manage.py migrate
```

6. **Create superuser (optional)**
```bash
python manage.py createsuperuser
```

7. **Run development server**
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

## Deployment on Railway

### Prerequisites

- Railway account (free at [railway.app](https://railway.app))
- GitHub account with repository

### Steps

1. **Initialize Git and push to GitHub**
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <your-github-repo-url>
git push -u origin main
```

2. **Connect Railway to GitHub**
   - Go to [railway.app](https://railway.app)
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your repository
   - Railway will auto-detect Django and create necessary services

3. **Configure Environment Variables in Railway**
   - Go to your project → Variables
   - Add the following:
     ```
     SECRET_KEY=your-very-secure-random-key
     DEBUG=False
     ALLOWED_HOSTS=your-railway-url.railway.app
     DATABASE_URL=postgresql://<user>:<password>@localhost/<db>
     EMAIL_HOST_USER=your-email@gmail.com
     EMAIL_HOST_PASSWORD=your-app-password
     ```

4. **Add PostgreSQL Plugin (Railway will prompt)**
   - Railway will automatically set `DATABASE_URL`
   - Update `settings.py` to use PostgreSQL in production (already configured)

5. **Deploy**
   - Railway auto-deploys on every git push to main branch
   - Check deployment logs in Railway dashboard

6. **Access Your Application**
   - Your app URL: `https://your-project-name.railway.app`

### Production Checklist

- ✅ `DEBUG = False`
- ✅ `SECRET_KEY` set in environment
- ✅ `ALLOWED_HOSTS` configured properly
- ✅ Database migrations run automatically
- ✅ Static files served via WhiteNoise
- ✅ Email backend configured

## Project Structure

```
hostel_hms_copy/
├── hostel/                 # Main Django app
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── urls.py            # URL routing
│   ├── forms.py           # Form definitions
│   ├── templates/         # HTML templates
│   └── utils/             # Utility functions
├── hostel_hms/            # Project settings
│   ├── settings.py        # Django configuration
│   ├── urls.py            # Project URLs
│   └── wsgi.py            # WSGI configuration
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── Procfile              # Railway deployment config
└── runtime.txt           # Python version
```

## Available Pages

- `/` - Landing page with portal selection
- `/login/` - Login page (Student/Authority roles)
- `/register/student/` - Student registration
- `/register/authority/` - Authority registration
- `/student_home/` - Student dashboard
- `/authority_home/` - Authority dashboard
- `/watchman/` - Watchman entry/exit portal
- `/admin/` - Django admin panel

## Default Credentials (Development)

Check `debug_users.py` for seed data.

## Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `SECRET_KEY` | Django secret key | `your-secret-key` |
| `DEBUG` | Debug mode | `False` |
| `ALLOWED_HOSTS` | Allowed hostnames | `localhost,127.0.0.1` |
| `DATABASE_URL` | Database connection | `postgresql://...` |
| `EMAIL_HOST_USER` | Gmail address | `your-email@gmail.com` |
| `EMAIL_HOST_PASSWORD` | Gmail app password | `abcd efgh ijkl mnop` |

## Troubleshooting

### Static files not loading
```bash
python manage.py collectstatic --noinput
```

### Database migration issues
```bash
python manage.py makemigrations
python manage.py migrate
```

### Email not sending
- Use Gmail with 2FA enabled
- Generate [app-specific password](https://myaccount.google.com/apppasswords)
- Check `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD` in `.env`

## Support

For issues or questions, please open an issue in the repository.

## License

This project is licensed under the MIT License.
