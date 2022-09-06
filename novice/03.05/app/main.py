# from crypt import methods
from ast import Delete
from flask import Flask, render_template
from flask import request
from flask import redirect
import psycopg2 
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
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
        curs.close()
        conn.close()
        
        # print(request.method)
        # print(20*"=")
        # print(request.form)
        # print(request.form["nama"])
        # print(request.form["detail"])
        # print(20*"=")

    print(request.method)   
    query = f"select * from buah"  
    curs.execute(query)  
    data = curs.fetchall() 
    # data = ["apel", "pear", "anggur"]
    return render_template("index.html", context=data)
@app.route("/detail/<buah_id>")
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

@app.route("/delete/<buah_id>")
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

@app.route("/update/<buah_id>")
def update(buah_id):
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="Alfi12345"
    )
    curs = conn.cursor()
    
    namaLama = 'pare'
    namaBaru = 'nanas'
    detailBaru = 'syegar'

    query = f"update buah set nama='{namaBaru}', detail='{detailBaru}' where nama ='{namaLama}'"
    curs.execute(query)
    conn.commit()
    print("data masuk")

    return redirect("/")   


if __name__ =="__main__":    
app.run()