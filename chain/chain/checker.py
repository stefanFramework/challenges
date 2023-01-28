class ChainChecker: 
    def list_is_chain(self, words): 
        if len(words) < 2:
            return False

        first_word = words[0]
        last_word = words[-1]

        if not self._are_words_chained(last_word, first_word):
            return False

        previous_word = None

        for current_word in words: 

            if previous_word is None:
                previous_word = current_word
                continue 

            if self._are_words_chained(previous_word, current_word):
                previous_word = current_word
           
        return True

    def _are_words_chained(self, previous_word, current_word):
        previous_last_character = self._get_last_character(previous_word)
        current_first_character = self._get_first_character(current_word)

        return True if previous_last_character == current_first_character else False

    def _get_last_character(self, word):
        return word[-1]

    def _get_first_character(self, word):
        return word[0]
