from flask import *
import sqlite3

app = Flask(__name__)
DATABASE = "database.db"

def create():
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS navy67(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL,
    password INTEGER NOT NULL)'''
    )
    conn.commit()
    conn.close()

@app.route("/", methods = ["POST", "GET"])
def insert():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute("INSERT INTO navy67(email, password) VALUES(?,?)", (email, password))
        conn.commit()
        conn.close()
        return redirect("/view")
    return render_template("login.html")

@app.route("/update/<int:id>", methods = ["POST", "GET"])
def update(id):
    conn = sqlite3.connect(DATABASE)
    cur  = conn.cursor()
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        cur.execute("UPDATE navy67 SET email = ?, password = ? WHERE id = ?",(email, password, id))
        conn.commit()
        conn.close()
        return redirect("/view")
    cur.execute("select * from navy67 where id = ?", (id,))
    single_rec = cur.fetchone()
    conn.close()
    return render_template("update.html", rec = single_rec)

@app.route("/delete/<int:id>", methods = ["POST","GET"])
def delete(id):
    conn =  sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("DELETE FROM navy67 WHERE id  = ?", (id,))
    conn.commit()
    conn.close()
    return redirect("/view")

@app.route("/view")
def view():
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("SELECT * FROM navy67")
    all_rec = cur.fetchall()
    conn.close()
    return render_template("view.html",  records = all_rec)


if __name__ == "__main__" :
    create()
    app.run(debug = True)
