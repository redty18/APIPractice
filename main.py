from flask import Flask

app = Flask(__name__)

@app.route('/name/<username>')
def hello_world(username):
    return f'Hello, {username}!'

@app.route('/home')
def homepage():
    return 'New Page'

@app.route('/about/<username>')
def about(username):
    return f"Information about {username}"

@app.route('/contact/<username>')
def contact(username):
    return f"{username}'s phone number"

emailDict = {}

@app.route('/register/<email>/<password>')
def addEmail(email, password):
    if email in emailDict:
        return f'{email} already exists, please register with a new one.'
    else:
        emailDict[email] = password
        return f"{email} was succesfully registered!"

@app.route("/login/<email>/<password>")
def login(email, password):
    if email in emailDict:
        checkPass = emailDict.get(email, None)
        if password == checkPass:
            return f"{email} was logged in!"
        else:
            return f"Wrong Password"
    else:
        return f"Email hasn't been registered yet."

@app.route("/logout/<email>")
def logout(email):
    if email in emailDict:
        del emailDict[email]
        return f"Logged out and account deleted succesfully."
    else:
        return f"{email} doesn't exist."
    
products = {
    1: {'name': 'Laptop', 'price': 1200},
    2: {'name': 'Phone', 'price': 500},
    3: {'name': 'Tablet', 'price': 300}
}
   
@app.route('/product/<int:product_id>/<string:category>')
def productList(product_id, category):
    product = products[product_id]
    product['category'] = category
    return f"{product['name']}, {product['price']}, {product['category']}"
    
if __name__ == "__main__":
    app.run(debug=True)