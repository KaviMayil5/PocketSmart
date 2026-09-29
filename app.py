from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():

    username = request.form.get("username")
    password = request.form.get("password")

    if username == "admin" and password == "1234":
        return render_template("dashboard.html")

    return "Invalid username or password"


@app.route("/interior")
def interior():
    return render_template("interior.html")


@app.route("/jewelry")
def jewelry():
    return render_template("jewelry.html")


@app.route("/party")
def party():
    return render_template("party.html")


@app.route("/products")
def products():

    jewelry_type = request.args.get("type", "Ring")

    metal = request.args.get("metal", "Gold")

    price = request.args.get("price", "")

    return render_template(
        "products.html",
        jewelry_type=jewelry_type,
        metal=metal,
        price=price
    )


if __name__ == "__main__":
    app.run(debug=True)