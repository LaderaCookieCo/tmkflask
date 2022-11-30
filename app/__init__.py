from flask import Flask
import os
app = Flask("game",template_folder="app/templates")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY") or "tree"
from app import routes