import sqlite3
from flask import Flask, render_template

app = Flask(__name__)


def get_connection():
    connection = sqlite3.connect("college.db")
    connection.row_factory = sqlite3.Row
    return connection


# ---------------- READ ----------------
@app.route("/")
def index():
    connection = get_connection()

    students = connection.execute(
        "SELECT * FROM students"
    ).fetchall()

    connection.close()

    return render_template("index.html", students=students)


# ---------------- CREATE ----------------
@app.route("/add")
def add():

    connection = get_connection()

    connection.execute(
        "INSERT INTO students(name, age) VALUES(?, ?)",
        ("Dhruv", 19)
    )

    connection.commit()
    connection.close()

    return "Student Added Successfully!"


# ---------------- UPDATE ----------------
@app.route("/update/<int:id>")
def update(id):

    connection = get_connection()

    connection.execute(
        "UPDATE students SET name=?, age=? WHERE id=?",
        ("Rahul", 22, id)
    )

    connection.commit()
    connection.close()

    return "Student Updated Successfully!"


# ---------------- DELETE ----------------
@app.route("/delete/<int:id>")
def delete(id):

    connection = get_connection()

    connection.execute(
        "DELETE FROM students WHERE id=?",
        (id,)
    )

    connection.commit()
    connection.close()

    return "Student Deleted Successfully!"


if __name__ == "__main__":
    app.run(debug=True)