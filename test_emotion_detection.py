
import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def test_joy(self):
        text = "I'm glad this happened"
        result = emotion_detector(text)
        print("Test Joy - Result:", result)
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger(self):
        text = "I'm really angry about this"
        result = emotion_detector(text)
        print("Test Anger - Result:", result)
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgust(self):
        text = "I feel disgusted just hearing about this"
        result = emotion_detector(text)
        print("Test Disgust - Result:", result)
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sadness(self):
        text = "I'm so sad about this"
        result = emotion_detector(text)
        print("Test Sadness - Result:", result)
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear(self):
        text = "I am very afraid that this will happen"
        result = emotion_detector(text)
        print("Test Fear - Result:", result)
        self.assertEqual(result['dominant_emotion'], 'fear')

if __name__ == "__main__":
    unittest.main()
