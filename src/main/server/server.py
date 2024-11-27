from flask import Flask
from flask_cors import CORS
from src.models.sqlite.settings.connection import db_connect_handle

from src.main.routes.legal_entity_routes import legal_entity_bp
from src.main.routes.natural_person_routes import natural_person_bp

db_connect_handle.connect_to_db()

app = Flask(__name__)
CORS(app)

app.register_blueprint(legal_entity_bp)
app.register_blueprint(natural_person_bp)