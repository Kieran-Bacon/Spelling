import collections
import itertools

class SpellingModel:
    """ Using the Hamming distance as the metric of fitness, propose correctly spelt words by selecting the closest
    correctly spelt word.

    Params:
        initial (iterable): The initial dictionary for the spelling model, must be acceptable as input into
            `collections.Counter` object
    """

    LONGESTWORDLENGTH = 50

    def __init__(self, initial: object = []):

        self._words = collections.Counter()
        self._lengths = self._lengths = {i: set() for i in range(1, self.LONGESTWORDLENGTH)}

        if initial:
            if isinstance(initial, str): initial = initial.split("")
            self.fit(initial)

    def fit(self, iterable: [str]) -> str:
        """ Fit the spelling model to the provided words. This shall update the dictionary to include new words and
        shall update their frequency.

        Params:
            iterable ([str]): A list of words that are to be added to the dictionary and their frequency recorded
        """
        self._words += collections.Counter(iterable)
        for word in iterable: self._lengths[len(word)].add(word)

    def predict(self, word: str) -> str:
        """ predict the correct spelling for the provided word and return

        Params:
            word (str): The word the be corrected according to this model
        """
        if word in self._words: return word  # The word does not need to be corrected

        length = len(word)  # The length of the word that is being predicted
        distance = 1  # The distance we are looking away from the word
        distances = {i: [] for i in range(1, self.LONGESTWORDLENGTH)}  # Structure for evaluated word distances
        while True:
            suspected = self._lengths[length + distance].union(self._lengths[length - distance])
            if distance == 1: suspected = suspected.union(self._lengths[length])

            # Find the hamming distance between the provided word and the suspected words
            for target in suspected:
                distances[self._hammingDistance(word, target)].append(target)

            # Return the word with the closest hamming distance, with the greatest probability
            if distances[distance]:
                return sorted(distances[distance], key=lambda x: self._words[x], reverse=True)[0]

            # Nothing was found, increase the distance that we are looking at
            distance += 1

    @classmethod
    def _hammingDistance(cls, a: str, b: str):
        """ An algorithm to find the distance between two words, the metric is the number of changes that would need to
        be made to convert one of the two into the other (this relationship is bidirectional)

        Params:
            a (str): The first word
            b (str): The second word
        """

        if len(a) != len(b):
            longer, smaller = sorted([a,b], key=lambda x: len(x), reverse=True)

            min_distance = len(smaller)
            for combination in itertools.combinations(longer, len(smaller)):
                distance = cls._hammingDistance(smaller, combination)
                if distance < min_distance: min_distance = distance

            return min_distance + len(longer) - len(smaller)

        return sum([i != j for i, j in zip(a, b)])