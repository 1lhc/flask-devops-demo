from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from DevOps demo!"

if __name__ == "__main__":
    app.run(debug=True)
