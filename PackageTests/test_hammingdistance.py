import unittest

from spelling import SpellingModel

class TestHammingDistance(unittest.TestCase):

    def test_hammingDistance(self):

        self.assertEqual(SpellingModel._hammingDistance("item1", "item2"), 1)
        self.assertEqual(SpellingModel._hammingDistance("different", "differ"), 3)

    def test_bidirectional(self):

        wordset = ["This", "is", "a", "word", "set"]
        wordset2 = ["Return", "of", "the", "word", "sets"]

        for w1, w2 in zip(wordset, wordset2):
            self.assertEqual(
                SpellingModel._hammingDistance(w1, w2),
                SpellingModel._hammingDistance(w2, w1)
            )