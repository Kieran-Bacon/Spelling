import unittest

import spelling

class TestNameSpace(unittest.TestCase):

    def test_predict(self):
        # As such because the built in model is not trained, only all words are added
        self.assertIn(spelling.predict("bway"), ["way", "bay", "away", "sway", "tway", "bray"])