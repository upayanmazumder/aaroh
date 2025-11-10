from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"message": "AI service is running!"})


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    # dummy response for now
    return jsonify({"input": data, "prediction": "This is a mock prediction 🚀"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
