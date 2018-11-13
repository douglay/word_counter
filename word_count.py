class WordCount:
    '''
    object-oriented word counter
    '''

    def __init__(self, fh):
        self._word_list = fh.read().strip().split()
        self._word_count = {}
        self._build_dictionary()

    def _build_dictionary(self):
        for word in self._word_list:
            if word in self._word_count:
                self._word_count[word] += 1
            else:
                self._word_count[word] = 1

    def get_all_unique_words(self):
        return sorted(set(self._word_list))

    def get_all_word_counts(self):
        return self._word_count

    def get_total_number_of_words(self):
        return len(self._word_list)

    @classmethod
    def create_from_file(cls, filename):
        with open(filename) as fh:
            return cls(fh)
