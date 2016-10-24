import unittest
from apriori_algorithm import AprioriAlgorithm


class AprioriAlgorithmTests(unittest.TestCase):
    def setUp(self):
        self.transactions = {(1, 2, 3, 4), (1, 2, 4), (1, 2),
                             (2, 3, 4), (2, 3), (3, 4), (2, 4)}
        self.frequent_1_large_itemsets = {(2,): 6, (3,): 4, (4,): 5}
        #self.frequent_2_large_itemsets

        self.frequent_itemsets = [(1, 2, 3), (1, 2, 4), (1, 3, 4), (1, 3, 5), (2, 3, 4)]
        self.expected_join_step_candidates = [(1, 2, 3, 4), (1, 3, 4, 5)]
        self.expected_pruning_step_candidates = [(1, 2, 3, 4)]

    def tearDown(self):
        self.transactions.clear()
        self.transactions = None

    def test__create_frequent_1_large_itemsets(self):
        # Arrange

        # Action
        result_dictionary = AprioriAlgorithm \
            .create_frequent_1_large_itemsets(self.transactions, 0.5)

        # Assert
        # expected_dictionary = { (2,): 6, (3,): 4, (4,): 5}
        self.assertTrue(result_dictionary == self.frequent_1_large_itemsets)

    def test_candidate_generate_join_step(self):
        result = AprioriAlgorithm.candidate_generate_join_step(self.frequent_itemsets)
        # expect = [(1,2,3,4), (1,3,4,5)]
        self.assertTrue(result == self.expected_join_step_candidates)

    def test_candidate_generate_pruning_step(self):
        result = AprioriAlgorithm \
            .candidate_generate_pruning_step(self.frequent_itemsets, self.expected_join_step_candidates)
        self.assertTrue(result, self.expected_pruning_step_candidates)


    def test_itemsets_in_transaction(self):
        candidates = AprioriAlgorithm.candidate_generate(sorted(self.frequent_1_large_itemsets))
        result = AprioriAlgorithm.create_frequent_itemsets(self.transactions, candidates, 0.5)
        self.assertTrue(result == {(2,4) : 4})

    def test_apriori_algorithm(self):
        result = AprioriAlgorithm.run(self.transactions, 0.5)
        self.assertTrue(result == {(2,):6, (3,):4, (4,): 5, (2,4): 4})
test_suit = unittest.TestLoader().loadTestsFromTestCase(AprioriAlgorithmTests)
unittest.TextTestRunner().run(test_suit)
