import unittest
from sentiment_analysis import sentiment_analyzer

class TestSentimentAnalyzer(unittest.TestCase):

    def test_valid_inputs(self):

        result_1 = sentiment_analyzer('I love working with Python')
        self.assertEqual(result_1['label'], 'SENT_POSITIVE')
        
        result_2 = sentiment_analyzer('I hate working with Python')
        self.assertEqual(result_2['label'], 'SENT_NEGATIVE')
        
        result_3 = sentiment_analyzer('I am neutral on Python')
        self.assertEqual(result_3['label'], 'SENT_NEUTRAL')

    def test_invalid_inputs(self):

        self.assertIsNone(sentiment_analyzer(''))
        
        self.assertIsNone(sentiment_analyzer('   '))
        
        self.assertIsNone(sentiment_analyzer('12345'))
        
        self.assertIsNone(sentiment_analyzer('!@#$%^'))

if __name__ == '__main__':
    unittest.main()