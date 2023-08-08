from flask import Flask

app = Flask(__name__)

@app.route("/<var>")
def homepage(var):
    return f"hello {var}, good to see you"

if (__name__) == "__main__":
    app.run(host="0.0.0.0")