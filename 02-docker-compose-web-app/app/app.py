import os
import time
from flask import Flask, jsonify
import psycopg2
from psycopg2 import OperationalError

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("POSTGRES_DB", "devops_demo")
DB_USER = os.getenv("POSTGRES_USER", "devops_user")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "devops_password")


def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
    )


def init_db():
    for _ in range(10):
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS visits (
                    id SERIAL PRIMARY KEY,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)
            conn.commit()
            cur.close()
            conn.close()
            return
        except OperationalError:
            time.sleep(2)


@app.route("/")
def home():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO visits DEFAULT VALUES;")
    conn.commit()

    cur.execute("SELECT COUNT(*) FROM visits;")
    visits = cur.fetchone()[0]

    cur.close()
    conn.close()

    return jsonify({
        "message": "Hello from Docker Compose web app!",
        "database": "PostgreSQL connected",
        "visits": visits
    })


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
