import psycopg2
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
app = Flask(__name__)

def index():
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="Alfi12345")
    curs = conn.cursor()

    
    if request.method == "POST":
        nama = request.form["nama"]
        detail = request.form["detail"]
        query = f"insert into buah(nama, detail) values('{nama}', '{detail}')"
        curs.execute(query)
        conn.commit()

    print(request.method)
    query = f"select * from buah"
    curs.execute(query)
    data = curs.fetchall()
    # data = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Ahad"]
    return render_template("index.html", context=data)

def detail(buah_id):
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="Alfi12345")

    curs = conn.cursor()
    query = f"select * from buah where id = {buah_id}"
    curs.execute(query)
    data = curs.fetchone()
    curs.close()
    conn.close()
    print(data)
    return render_template("detail.html", context=data)


def delete(buah_id):
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="Alfi12345")

    curs = conn.cursor()
    query = f"delete from buah where id = {buah_id}"
    curs.execute(query)
    conn.commit()
    curs.close()
    conn.close()
    return redirect("/")


def update(buah_id):
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="Alfi12345"
    )
    curs = conn.cursor()
    if request.method == "POST":
        nama = request.form.get("nama")
        detail = request.form.get("detail")

    
    # namaLama = 'pare'
    # namaBaru = 'nanas'
    # detailBaru = 'syegar'

        query = f"update buah set nama = '{nama}', detail = '{detail}' where id = {buah_id}" 
        curs.execute(query)
        conn.commit()
        # print("data masuk")
        return redirect("/")   

    query = f"select * from buah where id = {buah_id}"
    curs.execute(query)
    data = curs.fetchone()
    curs.close()
    conn.close()
    return render_template("update.html", context=data)
