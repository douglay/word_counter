from word_count import WordCount

class WordAndLetterCount (WordCount):

    def __init__(self, fh):
        super(WordAndLetterCount, self).__init__(fh)
        self._build_letter_dictionary()

    def _build_letter_dictionary(self):
        self._letter_count = {}
        for word in self._word_list:
            for letter in word:
                if letter in self._letter_count:
                    self._letter_count[letter] += 1
                else:
                    self._letter_count[letter] = 1

    def get_all_letter_counts(self):
        return self._letter_count

    def guw(self):
        return self.get_all_unique_words()
