# lyrics_to_slides

Flask app that turns lyrics into Google Slides. Paste lyrics, get a presentation link.

**Live app:** [web-production-3b3c5.up.railway.app](https://web-production-3b3c5.up.railway.app)

The web app lives in `frontend/`.

## Deploy on Railway

1. **Create a project** at [railway.app](https://railway.app) and connect this repo.

2. **Root directory (choose one):**
   - **Option A:** In Railway → your service → Settings → set **Root Directory** to `frontend`. Railway will use `frontend/Procfile` and `frontend/requirements.txt`.
   - **Option B:** Leave root as the repo root. The root `Procfile` and `requirements.txt` will be used (app runs from `frontend`).

3. **Variables:** In Railway → Variables, add:
   - `SECRET_KEY` – a long random string for session security (e.g. from `openssl rand -hex 32`).
   - (Optional) **PostgreSQL:** Add the "PostgreSQL" plugin to the project; Railway will set `DATABASE_URL`. The app will use it instead of SQLite.

4. **Deploy:** Push to your connected branch; Railway will build and deploy. Open the generated URL to use the app.

5. **Database (if using Postgres):** After first deploy, run migrations or create tables once (e.g. via Railway shell or a one-off):
   ```bash
   cd frontend && python -c "from app import app, db; app.app_context().push(); db.create_all()"
   ```
   Or use `flask db upgrade` if you add Flask-Migrate migrations later.

**Start command when Root Directory = frontend:** In Railway → Settings → set **Start Command** to: `gunicorn -b 0.0.0.0:$PORT run:app`
