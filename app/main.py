from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    return jsonify({"message": "Hello, World!"})


def run():
    app.run(host="0.0.0.0", port=8000)


if __name__ == "__main__":
    run()
