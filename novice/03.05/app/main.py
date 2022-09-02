# from crypt import methods
from flask import Flask, render_template
from flask import request
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

if __name__ =="__main__":    
    app.run()