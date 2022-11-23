from flask import Flask
app = Flask("game",template_folder="app/templates")
from app import routes