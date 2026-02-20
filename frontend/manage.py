"""Run Flask CLI. Usage: python manage.py recreate-db"""
import os
import sys

# Ensure app is loaded for Flask CLI
os.environ.setdefault("FLASK_APP", "run:app")

from flask.cli import main

if __name__ == "__main__":
    sys.argv = ["flask"] + (sys.argv[1:] or ["--help"])
    main()
