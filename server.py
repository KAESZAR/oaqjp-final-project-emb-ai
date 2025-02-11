"""  
This module contains the Flask application for emotion detection  
using text analysis.  
"""  

from flask import Flask, request, jsonify, render_template  
from EmotionDetection.emotion_detection import emotion_detector  

app = Flask("Emotion Detection")  


@app.route('/', methods=['GET'])  
def home():  
    """  
    Renders the home page.  

    Returns:  
        str: The HTML content of the home page.  
    """  
    return render_template('index.html')  


@app.route('/emotionDetector', methods=['GET'])  
def emotion_detector_route():  
    """  
    Processes the text provided by the user and returns the result of the  
    emotion detection.  

    Returns:  
        Response: The formatted response with detected emotions or an error message.  
    """  
    text_to_analyze = request.args.get('textToAnalyze')  

    if not text_to_analyze or not text_to_analyze.strip():  
        return jsonify({"error": "Invalid text! Please try again!"}), 400  

    try:  
        result = emotion_detector(text_to_analyze)  # Función que devuelve el resultado  
        
        if isinstance(result, dict) and 'dominant_emotion' in result:  
            if result['dominant_emotion'] is None :  
                return jsonify({"error": "Invalid text! Please try again!"}), 400  

            formatted_response = (  
                f"For the given phrase, the system's response is "  
                f"'anger': {result.get('anger', 0)}, "  
                f"'disgust': {result.get('disgust', 0)}, "  
                f"'fear': {result.get('fear', 0)}, "  
                f"'joy': {result.get('joy', 0)} and "  
                f"'sadness': {result.get('sadness', 0)}. "  
                f"The dominant emotion is {result['dominant_emotion']}."  
            )  

            return jsonify({"response": formatted_response}), 200  # Código de estado adecuado  

        return jsonify({"error": "Unexpected result format from emotion_detector."}), 500  

    except ValueError as error:  
        return jsonify({"error": f"An error occurred while processing the text: {str(error)}"}), 500  


if __name__ == "__main__":  
    app.run(debug=True)  # Ejecutar la aplicación Flask