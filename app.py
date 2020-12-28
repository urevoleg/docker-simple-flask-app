import os
import json
import datetime
from flask import Flask

app = Flask(__name__)

BASE_FOLDER = os.path.dirname(os.path.abspath(__file__))
RESOURCE_DIR = os.path.join(BASE_FOLDER, "resource")

@app.route('/')
def hello_world():
    print(request.args)
    with open(os.path.join(RESOURCE_DIR, "responce.json")) as f:
        return f"{json.loads(f.read()).get('payload')} - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9876, debug=True)