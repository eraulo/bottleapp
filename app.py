from bottle import Bottle, run

app = Bottle()

@app.route('/')
def home():
    return "Hello, Piku with Bottle!"

if __name__ == "__main__":
    run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

