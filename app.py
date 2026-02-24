from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient("mongodb+srv://shailesh:Shailesh123@cluster0.fkkg9xb.mongodb.net/?appName=Cluster0")
db = client["school"]
collection = db["students"]

@app.route("/")
def home():
    students = collection.find()
    return render_template("index.html", students=students)

@app.route("/add", methods=["POST"])
def add_student():
    name = request.form["name"]
    marks = int(request.form["marks"])
    collection.insert_one({"name": name, "marks": marks})
    return redirect("/")

@app.route("/delete/<id>")
def delete_student(id):
    collection.delete_one({"_id": ObjectId(id)})
    return redirect("/")

if __name__ == "__main__":
    app.run()