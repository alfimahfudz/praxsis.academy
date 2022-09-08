from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import psycopg2

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    conn = psycopg2.connect(
        host="localhost",
        database="puisiku",
        user="postgres",
        password="Alfi12345"
    )    
        
    
    curs = conn.cursor()    
    if request.method == "POST":
        judul = request.form.get("judul")
        sajak = request.form.get("sajak")
        query = f"insert into puisiku(judul, sajak) values('{judul}', '{sajak}')"
        curs.execute(query)
        conn.commit()

    print(request.method)
    query = f"select * from puisiku"
    curs.execute(query)
    data = curs.fetchall()
    curs.close()
    conn.close()
    return render_template("index.html", context=data)

@app.route("/detail/<puisiku_id>")
def detail(puisiku_id):
    conn = psycopg2.connect(
        host="localhost",
        database="puisiku",
        user="postgres",
        password="Alfi12345")
    
    curs = conn.cursor()
    query = f"select * from puisiku where id = {puisiku_id}"
    curs.execute(query)
    data = curs.fetchone()
    curs.close()
    conn.close()
    print(data)
    return render_template("detail.html", context=data)

@app.route("/delete/<puisiku_id>")
def delete(puisiku_id):
    conn = psycopg2.connect(
        host="localhost",
        database="puisiku",
        user="postgres",
        password="Alfi12345")
    
    curs = conn.cursor()
    query = f"delete from puisiku where id = {puisiku_id}"
    curs.execute(query)
    conn.commit()
    curs.close()
    conn.close()
    return redirect("/")

@app.route("/update/<puisiku_id>", methods=["GET", "POST"])
def update(puisiku_id):
    conn = psycopg2.connect(
        host="localhost",
        database="puisiku",
        user="postgres",
        password="Alfi12345")
    
    curs = conn.cursor()
    if request.method == "POST":
        judul = request.form["judul"]
        sajak = request.form["sajak"]
        
        query = f"update puisiku set judul = '{judul}', sajak = '{sajak}' where id = {puisiku_id}"
        curs.execute(query)
        conn.commit()
        return redirect("/")
    
    query = f"select * from puisiku where id = {puisiku_id}"
    curs.execute(query)
    data = curs.fetchone()
    curs.close()
    conn.close()
    return render_template("update.html", context=data)

if __name__ == "__main__":
    app.run()