import unittest
import translator

class TestTranslations(unittest.TestCase):
    '''Test translation from english to French and vice versa'''

    def test_english_to_french(self):
        '''translates english to french'''
        self.assertEqual(translator.english_to_french(''),'')
        self.assertEqual(translator.english_to_french('Hello'),
                          'Bonjour')
        self.assertEqual(translator.english_to_french('Hello friends'),
                          "Bonjour les amis")
        


    def test_french_to_english(self):
        '''translates french to english'''
        self.assertEqual(translator.french_to_english(''),'')
        self.assertEqual(translator.french_to_english('Bonjour'),
                         'Hello')
        self.assertEqual(translator.french_to_english("Bonjour les amis"),
                         'Hello friends')

if __name__ == '__main__':
    unittest.main()
