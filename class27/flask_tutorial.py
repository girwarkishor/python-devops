# web frameworks
from flask import Flask
from to_get_instances import Ec2Services
from flask import request, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

# POST http://127.0.0.1:5000/startec2
# Request Headers
# Content-Type: application/json
# User-Agent: PostmanRuntime/7.26.8
# Accept: */*
# Postman-Token: f5a46fc4-c97a-4689-be9f-063798d0563b
# Host: 127.0.0.1:5000
# Accept-Encoding: gzip, deflate, br
# Connection: keep-alive
# Request Body
# {"name":"kuna"}
@app.route('/startec2', methods=['POST'])
def start_instance():
    record = json.loads(request.data)
    print(record.get("name", "user hasn't given name"))
    trigger_aws = Ec2Services("name", "filter")
    instance_id = trigger_aws.create_ec2_instance()
    json_response = {"instance_id": str(instance_id.id)}
    return jsonify(json_response)



if __name__ == "__main__":
    app.debug = True
    app.run()