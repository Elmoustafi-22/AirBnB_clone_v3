#!/usr/bin/python3

import os
from flask import Flask
from models import storage
from api.v1.views import api_views
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

app.register_blueprint(api_views, url_prefix="/api/v1")

@app.teardown_appcontext
def close(ctx):
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    return {"error": "Not found"}, 404


@app.errorhandler(400)
def page_not_found(error):
    message = error.description
    return mesage, 400


if os.getenv("HBNB_API_HOST"):
    host = os.getenv("HBNB_API_HOST")
else:
    host = "0.0.0.0"

if os.getenv("HBNB_API_PORT"):
    host = os.getenv("HBNB_API_PORT")
else:
    port = 5000


if __name__ == "__main__":
    app.run(host=host, port=port, threaded=True)