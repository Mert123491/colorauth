import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def auth():
    key = request.args.get('key')
    machine_id = request.args.get('machine_id')

    if key == "ABC123" and machine_id == "MACHINE01":
        return "result=True"
    else:
        return "result=True"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
