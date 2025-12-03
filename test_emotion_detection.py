from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        self.assertEqual('joy', emotion_detector('I am really glad this happened')['dominant_emotion'])
        self.assertEqual('anger', emotion_detector('I am really mad about this')['dominant_emotion'])
        self.assertEqual('disgust', emotion_detector('I feel disgusted just hearing about this')['dominant_emotion'])
        self.assertEqual('sadness', emotion_detector('I am so sad about this')['dominant_emotion'])
        self.assertEqual('fear', emotion_detector('I am really afraid that this will happen')['dominant_emotion'])

unittest.main()