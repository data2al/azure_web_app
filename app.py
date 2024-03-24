from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


#setup web address
@app.route("/")
#create a home page and return some html
def mainpage():
    return render_template("index.html", content = ['Tim', 'Joe', 'Pain'])

@app.route("/home/")
def home():
    return "Hello! this is the second page <h1>HELLO<h1>"

# allows text to include user specific info
@app.route("/user/<name>/")
def user(name):
    return f"Hello {name}!"

# redirect users to a different page
@app.route("/admin/")
def admin():
    return redirect(url_for("user", name = "Admin!"))

# have the app run, may need to be removed on azure web app
if __name__ == "__main__":
    app.run(debug=True)