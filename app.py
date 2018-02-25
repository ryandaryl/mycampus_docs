import os
from flask import Flask
app = Flask(__name__)

class HelloWorld(object):
    def get(self):
        return {'hello': 'world'}

@app.route("/")
def hello():
    return "Hello from Python!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
