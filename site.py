from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def iplogger():
    print(request.remote_addr)
    return "пошёл нахуй"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
