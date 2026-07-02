async function predictPerformance() {
    const name = document.getElementById("studentName").value;
    const studyHours = Number(document.getElementById("studyHours").value);
    const attendance = Number(document.getElementById("attendance").value);
    const previousScore = Number(document.getElementById("previousScore").value);

    const loading = document.getElementById("loading");
    const result = document.getElementById("result");

    loading.innerHTML = "Sending request to backend...";
    result.innerHTML = "";

    try {
        const response = await fetch("http://127.0.0.1:5000/api/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                student_name: name,
                study_hours: studyHours,
                attendance: attendance,
                previous_score: previousScore
            })
        });

        const data = await response.json();

        loading.innerHTML = "";
        result.innerHTML = name + "'s Predicted Result: " + data.prediction +
            " | Final Score: " + data.final_score;

    } catch (error) {
        loading.innerHTML = "";
        result.innerHTML = "Backend connection failed. Please run Flask server first.";
    }
}
