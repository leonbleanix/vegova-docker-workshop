import importlib
import logging
import os

from flask import Flask, jsonify
import psycopg2
import psycopg2.extras

app = Flask(__name__)
logger = logging.getLogger("Server")


def get_db_connection():
    return psycopg2.connect(
        host=os.environ.get("DB_HOST", ""),
        port=os.environ.get("DB_PORT", "5432"),
        user=os.environ.get("DB_USER", ""),
        password=os.environ.get("DB_PASSWORD", ""),
        dbname=os.environ.get("DB_NAME", ""),
        connect_timeout=3,
    )

@app.route("/hello")
def hello():
    return jsonify({"message": "Hello, World!"})


@app.route("/db")
def db_check():
    try:
        conn = get_db_connection()
        conn.close()

        return jsonify({
            "message": "connected",
        })
    except Exception as e:
        logger.error(f"Database connection failed: {e}")

        return jsonify({
            "message": "unreachable",
            "error": str(e),
        }), 500


@app.route("/db/persist")
def db_persist():
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

        # Create table if it doesn't exist
        cur.execute("""
            CREATE TABLE IF NOT EXISTS visits (
                id SERIAL PRIMARY KEY,
                timestamp TIMESTAMPTZ DEFAULT NOW()
            )
        """)

        # Insert a new visit
        cur.execute("INSERT INTO visits DEFAULT VALUES")
        conn.commit()

        # Return all visits
        cur.execute("SELECT id, timestamp::text FROM visits ORDER BY id")
        rows = cur.fetchall()

        cur.close()
        conn.close()

        return jsonify({
            "message": "ok",
            "visits": [dict(row) for row in rows],
        })
    except Exception as e:
        logger.error(f"Database persist failed: {e}")

        return jsonify({
            "message": "error",
            "error": str(e),
        }), 500


@app.route("/production-check")
def production_check():
    issues = []

    # Check if dev dependencies are installed
    try:
        importlib.import_module("pytest")
        issues.append("Dev dependency 'pytest' is installed")
    except ImportError:
        pass

    # Check if running as root
    if os.getuid() == 0:
        issues.append("Running as root user")

    # Check if non-production files/directories exist
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Tests shouldn't be in the production image.
    if os.path.isdir(os.path.join(base_dir, "tests")):
        issues.append("'tests/' directory exists")

    # Dockerfile shouldn't be in the production image.
    if os.path.isfile(os.path.join(base_dir, "Dockerfile")):
        issues.append("'Dockerfile' exists")

    # Tasks shouldn't be in the production image.
    if os.path.isdir(os.path.join(base_dir, "tasks")):
        issues.append("'tasks/' directory exists")

    if issues:
        return jsonify({
            "message": "not production-ready",
            "issues": issues,
        })

    return jsonify({
        "message": "production-ready",
    })


def run():
    app.run(host="0.0.0.0", port=8000)


if __name__ == "__main__":
    run()
