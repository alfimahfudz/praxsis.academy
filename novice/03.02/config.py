import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="suppliers",
        user="postgres",
        password="Alfi12345")