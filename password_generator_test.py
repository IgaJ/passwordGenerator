import unittest
import string
from password_generator import generate


class TestPasswordGenerator(unittest.TestCase):
    def test_generate_length(self):
        length = 12
        password = generate(length)
        self.assertEqual(len(password), length)

    def test_generate_characters(self):
        length = 12
        password = generate(length)
        all_characters = string.ascii_letters + string.digits + string.punctuation
        for char in password:
            self.assertIn(char, all_characters)


if __name__ == '__main__':
    unittest.main()
