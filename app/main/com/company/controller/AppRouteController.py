import json

from flask import Flask, request
from app.main.com.company.utils.ProjectConstants import model_token


app = Flask(__name__)


@app.route('/api/public/generateuml', methods=['POST'])
def post_generate_uml():

    request_json = json.loads(request.data)
    token = model_token
    

    return
