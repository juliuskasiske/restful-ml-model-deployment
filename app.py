from flask import flask

app = flask(__name__)

@app.route("/")
def homepage():
    pass

if (__name__) == "__main__":
    app.run()