from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def auth():
    key = request.args.get('key')
    machine_id = request.args.get('machine_id')

    if key == "liwu" and machine_id == "liwu":
        return "True"
    else:
        return "True"
