import os

from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)


@app.route("/hello")
def hello():
    return jsonify({"message": "Hello, World!"})


@app.route("/db")
def db_check():
    try:
        # Try to connect to the database
        conn = psycopg2.connect(
            host=os.environ.get("DB_HOST", ""),
            port=os.environ.get("DB_PORT", "5432"),
            user=os.environ.get("DB_USER", ""),
            password=os.environ.get("DB_PASSWORD", ""),
            dbname=os.environ.get("DB_NAME", ""),
            connect_timeout=3,
        )

        conn.close()

        return jsonify({
            "message": "connected",
        })
    except Exception as e:
        # If the connection fails, return an error message
        return jsonify({
            "message": "unreachable",
            "error": str(e),
        })


def run():
    app.run(host="0.0.0.0", port=8000)


if __name__ == "__main__":
    run()
