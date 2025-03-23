from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def auth():
    key = request.args.get('key')
    machine_id = request.args.get('machine_id')

    if key == "ABC123" and machine_id == "XYZ987":
        return "valid"
    else:
        return "invalid"

# 🔥 BURASI ÖNEMLİ!
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
