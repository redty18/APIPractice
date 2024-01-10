from flask import Flask, request, jsonify

app = Flask(__name__)

class loginDetails():
    def __init__(self, emailID, password):
        self.emailID = emailID
        self.password = password
        self.isLoggedIn = False
        self.listOfToDoID = []
    
    def addToList(self, toDoID):
        self.listOfToDoID.append(toDoID)

class ToDo():
    def __init__(self, toDoID, toDo, emailID):
        self.toDoID = toDoID
        self.toDo = toDo
        self.emailID = emailID

def checkIfLogin(email):
    for user in userList:
        if user.emailID == email and user.isLoggedIn:
            return True
    return False

toDoList = []

userList = []

@app.route("/register", methods = ['POST'])
def register():
    data = request.get_json()
    email = data.get("Email")
    password = data.get("Password")
    for string in userList:
        if email == string.emailID:
            return f"Already registered with {email}, please login."
    
    user1 = loginDetails(emailID=email, password=password)
    userList.append(user1)
    return "Registered"

@app.route("/login", methods = ['POST'])
def login():
    data = request.get_json()
    email = data.get("Email")
    password = data.get("Password")
    for string in userList:
        if email == string.emailID:
            if password == string.password:
                string.isLoggedIn = True
                return f"Succesfully logged in with {email}"
    return f"Incorrect credentials"

@app.route("/addToDo", methods = ['POST'])
def addToDo():
    data = request.get_json()
    toDoID = data.get("ToDoID")
    toDO = data.get("ToDo")
    email = data.get("Email")
    for ID in toDoList:
        if toDoID == ID.toDoID:
            return f"This ID already exists, choose another number"
    if checkIfLogin(email) == True:
        toDo1 = ToDo(toDoID=toDoID, toDo=toDO, emailID=email)
        toDoList.append(toDo1)
        return f"ToDo Added" 
    return "User not logged in."

@app.route("/deleteToDo", methods = ['POST'])
def deleteToDo():
    data = request.get_json()
    toDoID = data.get("ToDoID")
    email = data.get("Email")
    if checkIfLogin(email) == True:
        for ID in toDoList:
            if toDoID == ID.toDoID:
                toDoList.remove(ID)
                return f"ToDo Removed"
        return f"This ID is incorrect and does not belong to the user."
    return f"This ID doesn't exist, can't delete it, choose a different ID"

@app.route("/updateToDo", methods = ['POST'])
def updateToDo():
    data = request.get_json()
    toDoID = data.get("ToDoID")
    updatedToDo = data.get("UpdatedToDo")
    email = data.get("Email")
    if checkIfLogin(email) == True:
        for ID in toDoList:
            if toDoID == ID.toDoID and email == ID.emailID:
                ID.toDo = updatedToDo
                return "ToDo Updated"
        return f"This ID is incorrect and does not belong to the user."
    return f"This ID doesn't exist, can't delete it, choose a different ID"

if __name__ == "__main__":
    app.run(debug=True)