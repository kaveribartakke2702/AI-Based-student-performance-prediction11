from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

conversation_history = []

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

    student_name = data.get("student_name", "Student")
    study_hours = float(data.get("study_hours", 0))
    attendance = float(data.get("attendance", 0))
    previous_score = float(data.get("previous_score", 0))

    final_score = (study_hours * 10 + attendance + previous_score) / 3

    if final_score >= 75:
        prediction = "Good Performance"
    elif final_score >= 50:
        prediction = "Average Performance"
    else:
        prediction = "Poor Performance"

    response = {
        "student_name": student_name,
        "prediction": prediction,
        "final_score": round(final_score, 2),
        "status": "success"
    }

    conversation_history.append({
        "input": data,
        "output": response
    })

    return jsonify(response)

@app.route("/api/history", methods=["GET"])
def get_history():
    return jsonify({
        "status": "success",
        "history": conversation_history
    })

if __name__ == "__main__":
    app.run(debug=True)
