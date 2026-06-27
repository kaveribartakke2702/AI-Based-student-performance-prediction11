from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route("/")
def home():
    return jsonify({
        "message": "AI-Based Student Performance Prediction Backend is Running!"
    })
  @app.route("/api/health", methods=["GET"])
def health_check():
    return jsonify({
        "status": "success",
        "message": "Backend server is healthy"
    })
  @app.route("/api/predict", methods=["POST"])
def predict_performance():
    data = request.get_json()

    study_hours = data.get("study_hours", 0)
    attendance = data.get("attendance", 0)
    previous_score = data.get("previous_score", 0)

    average_score = (study_hours * 10 + attendance + previous_score) / 3

    if average_score >= 75:
        prediction = "Good Performance"
    elif average_score >= 50:
        prediction = "Average Performance"
    else:
        prediction = "Poor Performance"

    return jsonify({
        "status": "success",
        "prediction": prediction,
        "average_score": round(average_score, 2)
    })
  if __name__ == "__main__":
    app.run(debug=True)
