from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()

connection = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    user=os.getenv("DB_USERNAME"),
    password=os.getenv("DB_PASSWORD"),
    dbname=os.getenv("DB_NAME"),
    sslmode="require",
    sslrootcert=os.getenv("CA_CERT_PATH", "ca-certificate.crt"),
)
