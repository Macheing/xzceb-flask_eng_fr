'''Import Unit testing library and the module to be tested'''
import unittest
from translator import english_to_french, french_to_english

class TestTranslations(unittest.TestCase):
    '''Test translation from english to French and vice versa'''

    def test_english_to_french(self):
        '''translates english to french'''
        self.assertEqual(english_to_french(''),'')
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        self.assertEqual(english_to_french("Hello friends"),"Bonjour amis")

    def test_french_to_english(self):
        '''translates french to english'''
        self.assertEqual(french_to_english(''),'')
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        self.assertEqual(french_to_english("Bonjour amis"),'Hello friends')

if __name__ == '__main__':
    unittest.main()
