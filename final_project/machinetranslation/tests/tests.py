import unittest

from translator import french_to_english, english_to_french

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        try:
            self.assertNotEqual(french_to_english(None), "")
        except ValueError:
            print("text is None")
        except:
            print("Error")

        self.assertEqual(french_to_english("Bonjour"), "Hello")


class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        try:
            self.assertNotEqual(english_to_french(None), "")
        except ValueError:
            print("text is None")
        except:
            print("Error")

        self.assertEqual(english_to_french("Hello"), "Bonjour")


unittest.main()
