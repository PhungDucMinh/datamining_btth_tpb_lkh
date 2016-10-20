import unittest
from apriori_algorithm import AprioriAlgorithm


class AprioriAlgorithmTests(unittest.TestCase):
    def setUp(self):
        self.transaction_list = {(1, 2, 3, 4), (1, 2, 4), (1, 2),
                                 (2, 3, 4), (2, 3), (3, 4), (2, 4)}

    def tearDown(self):
        self.transaction_list.clear()
        self.transaction_list = None

    def test_determine_set_of_frequent_1_item_sets(self):
        # Arrange

        aprior_algorithm = AprioriAlgorithm()
        # Action
        result_dictionary = aprior_algorithm \
            .create_frequent_1_item_set(self.transaction_list, 0.5)

        # Assert
        expected_dictionary = {1: 3, 2: 6, 3: 4, 4: 5}
        self.assertTrue(result_dictionary, expected_dictionary)


test_suit = unittest.TestLoader().loadTestsFromTestCase(AprioriAlgorithmTests)
unittest.TextTestRunner().run(test_suit)
