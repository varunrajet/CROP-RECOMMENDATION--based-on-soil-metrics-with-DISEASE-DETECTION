// Event listener for form submission
$("#soil-form").on("submit", function(event) {
    event.preventDefault();

    // Collect input data
    const inputData = {
        nitrogen: $("#nitrogen").val(),
        phosphorus: $("#phosphorus").val(),
        potassium: $("#potassium").val(),
        temperature: $("#temperature").val(),
        humidity: $("#humidity").val(),
        ph_value: $("#ph_value").val(),
    };

    // Fetch crop prediction
    fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(inputData),
    })
        .then((response) => response.json())
        .then((data) => {
            $("#result").text(
                data.prediction ? `Predicted Crop: ${data.prediction}` : `Error: ${data.error}`
            );

            // Fetch disease prediction based on soil data
            return fetch("http://127.0.0.1:5000/disease", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(inputData),
            });
        })
        .then((response) => response.json())
        .then((diseaseData) => {
            $("#disease-result").text(
                diseaseData.diseases
                    ? `Potential Diseases: ${diseaseData.diseases.join(", ")}`
                    : `Error: ${diseaseData.error}`
            );
        })
        .catch((error) => {
            $("#result").text(`An error occurred: ${error.message}`);
            $("#disease-result").text("Could not fetch disease predictions.");
        });
});
