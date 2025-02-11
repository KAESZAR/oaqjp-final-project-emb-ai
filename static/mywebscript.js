let RunSentimentAnalysis = ()=>{
    let textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
            if (this.status == 200) {
                document.getElementById("system_response").innerHTML = JSON.parse(xhttp.responseText).response;
            } else if (this.status == 400 || this.status == 500) {
                document.getElementById("system_response").innerHTML = JSON.parse(xhttp.responseText).error;
            }
        }
    };
    xhttp.open("GET", "emotionDetector?textToAnalyze=" + textToAnalyze, true);
    xhttp.send();
}
