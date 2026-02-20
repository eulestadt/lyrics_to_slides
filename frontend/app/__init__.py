"""
Initialize the Flask application
"""
# Python 3.10+: MutableMapping moved to collections.abc; old uritemplate expects collections.MutableMapping
import collections
import collections.abc
if not hasattr(collections, "MutableMapping"):
    collections.MutableMapping = collections.abc.MutableMapping

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# On Railway: create secret.json from env so OAuth works (no file upload)
_creds_json = os.environ.get("GOOGLE_OAUTH_CREDENTIALS_JSON")
if _creds_json:
    _secret_path = os.path.join(os.getcwd(), "secret.json")
    with open(_secret_path, "w") as f:
        f.write(_creds_json)

# Create database
db = SQLAlchemy()

# Initialize the application
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-change-in-production')

# Configure the application with database information
database_url = os.environ.get('DATABASE_URL', 'sqlite:///flask-data.db')
# Railway/Heroku use postgres:// but SQLAlchemy 1.4+ expects postgresql://
if database_url.startswith('postgres://'):
    database_url = 'postgresql://' + database_url[10:]
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Create tables if they don't exist (e.g. first deploy with Postgres on Railway)
with app.app_context():
    db.create_all()

# Import the views/routes
from . import views

# CLI (optional)
import click

@app.cli.command("recreate-db")
def recreate_db():
    """Recreate the database tables."""
    db.drop_all()
    db.create_all()
    db.session.commit()
    click.echo("Database recreated.")
