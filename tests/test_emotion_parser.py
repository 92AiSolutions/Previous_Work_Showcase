import unittest
from app.controllers.emotion_parser import parse_emotions

class TestEmotionParser(unittest.TestCase):
    def test_parsing(self):
        text = "[Luca] (soft): Hello world"
        parsed = parse_emotions(text)
        self.assertEqual(parsed[0]["character"], "Luca")
        self.assertEqual(parsed[0]["emotion"], "soft")
        self.assertEqual(parsed[0]["text"], "Hello world")

if __name__ == "__main__":
    unittest.main()
