import unittest
from apriori_algorithm import AprioriItem
from apriori_algorithm import AprioriItemSet


class AprioriAlgorithmTests(unittest.TestCase):
    def setUp(self):
        self.transaction_list = {(1, 2, 3, 4), (1, 2, 4), (1, 2),
                                 (2, 3, 4), (2, 3), (3, 4), (2, 4)}

    def tearDown(self):
        self.transaction_list.clear()
        self.transaction_list = None

    def test_determine_set_of_frequent_1_item_sets(self):

        # Arrange
        item_set_dictionary = {}

        # Action
        for transaction in self.transaction_list:
            for item in transaction:
                if not item_set_dictionary.has_key(item):
                    item_set_dictionary[item] = 1
                else:
                    item_set_dictionary[item] += 1

        # Assert
        result_dictionary = {1: 3, 2: 6, 3: 4, 4: 5}
        self.assertTrue(item_set_dictionary, result_dictionary)


test_suit = unittest.TestLoader().loadTestsFromTestCase(AprioriAlgorithmTests)
unittest.TextTestRunner().run(test_suit)
