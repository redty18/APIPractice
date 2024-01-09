from flask import Flask, request, jsonify

app = Flask(__name__)

app.route("/addToDo", methods = ['POST'])
def addToDo():
    data = request.get_json()
    pass