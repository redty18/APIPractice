from flask import Flask, request, jsonify

app = Flask(__name__)

class loginDetails:
    def __init__(self, stringID, stringPassword):
        self.stringID = stringID
        self.stringPassword = stringPassword
        self.isLoggedIn = False

products = {
    1: {'name': 'Laptop', 'price': 1200},
    2: {'name': 'Phone', 'price': 500},
    3: {'name': 'Tablet', 'price': 300}
}

userList = []

@app.route("/register/<stringID>/<stringPassword>")
def register(stringID, stringPassword):
    for obj in userList:  
        if stringID == obj.stringID:
            return f"{stringID} already exists, please login instead."
    
    person1 = loginDetails(stringID=stringID,stringPassword=stringPassword)
    userList.append(person1)
    return "Registration Complete"

@app.route('/login/<stringID>/<stringPassword>')
def login(stringID, stringPassword):
    for objID in userList:
        if stringID == objID.stringID and stringPassword == objID.stringPassword:
            objID.isLoggedIn = True
            return f"{stringID} has succesfully logged in!"
    return f"Incorrect Email or Password"

@app.route("/showProduct/<stringID>")
def showProductGet(stringID):
    for objID in userList:
        if stringID == objID.stringID:
            if objID.isLoggedIn == True:
                return products
    return f"Please login first to view the products"

@app.route('/showProduct', methods=['POST'])
def showProductPost():
    data = request.get_json()
    for objID in userList:
        if data.get("email") == objID.stringID:
            if objID.isLoggedIn == True:
                return products
    return f"Please login first to view the products"

@app.route('/showProductbyID', methods=['POST'])
def showByProdID():
    data = request.get_json()
    email = data.get("email")
    productID = data.get("productID")
    for objID in userList:
        if email == objID.stringID:
            if objID.isLoggedIn == True:
                return products.get(productID, None)
    return f"Please login first to view the products"

if __name__ == "__main__":
    app.run(debug=True)

