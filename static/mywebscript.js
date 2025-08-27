const runSentimentAnalysis = () => {

    const textToAnalyze = document.getElementById("textToAnalyze").value;


    const resultDiv = document.getElementById("system_response");

    fetch(`/sentimentAnalyzer?textToAnalyze=${encodeURIComponent(textToAnalyze)}`)
        .then(response => {

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            return response.text();
        })
        .then(data => {

            resultDiv.innerHTML = data;
            resultDiv.style.display = 'block';

            if (data.includes("POSITIVE")) {
                resultDiv.className = "mt-6 p-4 border-l-4 border-green-500 bg-green-50 rounded-r-lg";
            } else if (data.includes("NEGATIVE")) {
                resultDiv.className = "mt-6 p-4 border-l-4 border-red-500 bg-red-50 rounded-r-lg";
            } else {
                resultDiv.className = "mt-6 p-4 border-l-4 border-gray-400 bg-gray-50 rounded-r-lg";
            }
        })
        .catch(error => {

            console.error('Error:', error);
            resultDiv.innerHTML = "An error occurred while analyzing the text.";
            resultDiv.style.display = 'block';
            resultDiv.className = "mt-6 p-4 border-l-4 border-red-500 bg-red-50 rounded-r-lg";
        });
};