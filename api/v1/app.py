#!/usr/bin/python3
'''
    api
'''
from api.v1.views import app_views
from flask_cors import CORS
from flask import Flask, Blueprint, jsonify, make_response
from models import storage
import os


app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={'/*': {'origins': '0.0.0.0'}})

@app.teardown_appcontext
def teardown_appcontext(code):
    '''
        task #3
        calls storage.close()
    '''
    storag.close()

@app.errorhandler(404)
def page_not_found(error):
    '''
        returns error 404; not found
    '''
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == "__main__":
    app.run(host=os.getenv('HBNB_API_HOST', '0.0.0.0'),
            port = int(os.getenv('HBNB_API_PORT','5000')))
