from unittest import TestCase
from chain.checker import ChainChecker 

class ChainCheckerTest(TestCase):
    
    def setUp(self) -> None:
        self.checker = ChainChecker()
        return super().setUp()

    def test_empty_list_return_false(self):
        assert self.checker.list_is_chain([]) is False
    
    def test_chained_list_returns_true(self):
        assert self.checker.list_is_chain(['chair', 'razor', 'rocket', 'tunic']) is True

    def test_not_chained_list_returns_false(self):
        assert self.checker.list_is_chain(['chair', 'razor', 'rocket']) is False

    def test_single_word_list_returns_false(self):
        assert self.checker.list_is_chain(['nemo']) is False