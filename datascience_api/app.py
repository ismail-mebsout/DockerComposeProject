from flask import Flask, jsonify, request

FLASK_API = Flask(__name__)


def get_params(request):
    a = float(request.args["a"])
    b = float(request.args["b"])
    return a, b


@FLASK_API.route("/add", methods=["GET", "POST"])
def add():
    a, b = get_params(request)
    response = {"result": a + b}
    return jsonify(response)


if __name__ == "__main__":
    FLASK_API.debug = True
    FLASK_API.run(host="0.0.0.0", port="8080")
