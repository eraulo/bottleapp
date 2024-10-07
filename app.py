import os
from bottle import Bottle, run

app = Bottle()

@app.route('/')
def home():
    return "Hello, Piku!"


if __name__ == "__main__":
    # Use the port provided by Piku
    port = int(os.getenv('PORT', 8080))
    run(app, host='0.0.0.0', port=port)


