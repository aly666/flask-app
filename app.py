from flask import Flask
import psycopg2, os

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "postgres-0.postgres.postgres-ha.svc.cluster.local")
DB_NAME = os.getenv("DB_NAME", "postgres")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "")

@app.route("/")
def index():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            connect_timeout=5
        )
        cur = conn.cursor()
        cur.execute("SELECT version();")
        version = cur.fetchone()[0]
        cur.close()
        conn.close()
        return f"<h2>✅ Koneksi ke PostgreSQL Berhasil!</h2><p>{version}</p>"
    except Exception as e:
        return f"<h2>❌ Gagal konek ke PostgreSQL</h2><pre>{e}</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

