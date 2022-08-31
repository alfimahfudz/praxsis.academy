try:
    import psycopg2
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="Alfi12345")

except Exception as e:
    print(e)

curs = conn.cursor()
query = f"select * from siswa where umur=23" # where berarti menampilkan data yang detail
curs.execute(query)
data = curs.fetchone()

if not data:
    print("gada say")
else:
    print("nama:", data[0], "umur:", data[1])