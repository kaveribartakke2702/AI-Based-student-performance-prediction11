function predictPerformance() {
    const name = document.getElementById("studentName").value;
    const studyHours = Number(document.getElementById("studyHours").value);
    const attendance = Number(document.getElementById("attendance").value);
    const previousScore = Number(document.getElementById("previousScore").value);

    const loading = document.getElementById("loading");
    const result = document.getElementById("result");

    loading.innerHTML = "Predicting performance...";
    result.innerHTML = "";

    setTimeout(function () {
        const averageScore = (studyHours * 10 + attendance + previousScore) / 3;

        let prediction = "";

        if (averageScore >= 75) {
            prediction = "Good Performance";
            result.style.backgroundColor = "#d4edda";
            result.style.color = "#155724";
        } else if (averageScore >= 50) {
            prediction = "Average Performance";
            result.style.backgroundColor = "#fff3cd";
            result.style.color = "#856404";
        } else {
            prediction = "Poor Performance";
            result.style.backgroundColor = "#f8d7da";
            result.style.color = "#721c24";
        }

        loading.innerHTML = "";
        result.innerHTML = name + "'s Predicted Result: " + prediction;
    }, 1000);
}
