import unittest
import textExample

class TestCap(unittest.TestCase):
    def text_one_word(self):
        text = 'python'
        result = textExample.cap_text(text)
        self.assertEqual(result, 'Python')

    def text_multiple_word(self):
        text = 'python program'
        result = textExample.cap_text(text)
        self.assertEqual(result, 'Python Program')

        
if __name__ == '__main__':
    unittest.main()

