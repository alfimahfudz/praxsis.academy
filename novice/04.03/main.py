from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    conn = psycopg2.connect(
        host="localhost",
        database="puisi",
        user="postgres",
        password="Alfi12345"
    )
    curs = conn.cursor()
    if request.method == "POST":
        judul = request.form.get("judul")
        detail = request.form.get("detail")
        query = f"insert into puisi(judul, detail) values('{judul}', '{detail}')"
        curs.execute(query)
        conn.commit()

    print(request.method)
    query = f"select * from puisi"
    curs.execute(query)
    data = curs.fetchall()
    curs.close()
    conn.close()
    return render_template("index.html", context=data)  

if __name__ == "__main__":
    app.run()