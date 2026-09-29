from EmotionDetection.emotion_detection import emotion_detector #import function from package
import unittest #import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        result_1 = emotion_detector("I am glad this happened") #test 1 "I am glad this happened" , joy
        self.assertEqual(result_1["dominant emotion"],"joy")
        result_2 = emotion_detector("I am really mad about this") #test 2 "I am really mad about this" , anger
        self.assertEqual(result_2["dominant emotion"],"anger")
        result_3 = emotion_detector("I feel disgusted just hearing about this") #test 3 "I feel disgusted just hearing about this" , disgust
        self.assertEqual(result_3["dominant emotion"],"disgust")
        result_4 = emotion_detector("I am so sad about this") #test 4 "I am so sad about this" , sadness
        self.assertEqual(result_4["dominant emotion"],"sadness")
        result_5 = emotion_detector("I am really afraid that this will happen") #test 5 "I am really afraid that this will happen" , fear
        self.assertEqual(result_5["dominant emotion"],"fear")

unittest.main()