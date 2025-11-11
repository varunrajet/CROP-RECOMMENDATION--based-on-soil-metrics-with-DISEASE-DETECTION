
(function () {
  const form = document.getElementById("soil-form");
  const resultEl = document.getElementById("result");
  const diseaseEl = document.getElementById("diseases");

  const BACKEND = "http://127.0.0.1:5005";

  function setStatus(msgResult, msgDisease) {
    if (msgResult !== undefined) resultEl.textContent = msgResult;
    if (msgDisease !== undefined) diseaseEl.textContent = msgDisease;
  }

  form.addEventListener("submit", async function (e) {
    e.preventDefault();

    const payload = {
      nitrogen: Number(document.getElementById("nitrogen").value),
      phosphorus: Number(document.getElementById("phosphorus").value),
      potassium: Number(document.getElementById("potassium").value),
      temperature: Number(document.getElementById("temperature").value),
      humidity: Number(document.getElementById("humidity").value),
      ph_value: Number(document.getElementById("ph_value").value),
    };

    for (const k of ["nitrogen", "phosphorus", "potassium", "temperature", "humidity", "ph_value"]) {
      if (payload[k] === "" || Number.isNaN(payload[k])) {
        setStatus("Please enter valid numeric values for all fields.", "");
        return;
      }
    }

    try {
      setStatus("Predicting...", "Fetching disease predictions...");
      const resp = await fetch(`${BACKEND}/predict`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });

      if (!resp.ok) {
        let errText = `HTTP ${resp.status}`;
        try {
          const errJson = await resp.json();
          if (errJson && errJson.error) errText = errJson.error;
        } catch (_) {}
        throw new Error(errText);
      }

      const data = await resp.json();

      if (data && data.prediction) {
        const crop = data.prediction.crop ?? "N/A";
        const disease = data.prediction.disease ?? "N/A";
        setStatus(`Predicted Crop: ${crop}`, `Potential Diseases: ${disease}`);
      } else if (data && data.error) {
        setStatus(`Error: ${data.error}`, "");
      } else {
        setStatus("Unexpected response from server.", "");
      }
    } catch (err) {
      console.error("Prediction error:", err);
      setStatus(`An error occurred: ${err.message}`, `Could not fetch disease predictions: ${err.message}`);
    }
  });
})();
