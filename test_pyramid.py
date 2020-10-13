import unittest
from pyramid import is_pyramid_word

class TestPyramid(unittest.TestCase):
    def test_pyramid_empty_text_is_false(self):
        text = ""
        result = is_pyramid_word(text)
        self.assertFalse(result)

    def test_pyramid_word_valid_text_has_tabs_is_true(self):
        text = "banana\t"
        result = is_pyramid_word(text)
        self.assertTrue(result)

    def test_pyramid_word_invalid_text_has_tabs_is_false(self):
        text = "catalina\t"
        result = is_pyramid_word(text)
        self.assertFalse(result)

    def test_pyramid_word_valid_text_is_true(self):
        text = "banana"
        result = is_pyramid_word(text)
        self.assertTrue(result)

    def test_pyramid_word_valid_text_nonpyramid_is_false(self):
        text = "familia"
        result = is_pyramid_word(text)
        self.assertFalse(result)

    def test_pyramid_word_invalid_input_is_false(self):
        text = 1
        result = is_pyramid_word(text)
        self.assertFalse(result)
        

if __name__ == '__main__':
    unittest.main()