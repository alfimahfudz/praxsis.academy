try:
    import psycopg2
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="Alfi12345")

    curs = conn.cursor()
    query = f"insert into siswa(nama, umur) values('syahrin', 21)"
    curs.execute(query)
    conn.commit()
    print("data masuk")

except Exception as e:
    print(e)