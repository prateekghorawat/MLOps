from flask import Flask

###WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to My attempt to use and learn Flask"

@app.route("/hope")
def index():
    return "Hoping to Understand MLOps good"


if __name__=="__main__":
    app.run(debug=True)