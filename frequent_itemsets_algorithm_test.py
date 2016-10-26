import unittest
from apriori_algorithm import AprioriAlgorithm


class AprioriAlgorithmTests(unittest.TestCase):
    def setUp(self):
        self.transactions = {(1, 2, 3, 4), (1, 2, 4), (1, 2),
                             (2, 3, 4), (2, 3), (3, 4), (2, 4)}
        self.frequent_1_large_itemsets = {(2,): 6, (3,): 4, (4,): 5}
        self.frequent_itemsets_dictionary_3 = {("Bread", "Cheese", "Juice") : 0.7, ("Milk", "Bread", "Yogurt") : 0.7
                                               , ("Bread", "Juice", "Milk") : 0.7, ("Eggs", "Bread", "Cheese", "Juice") :0.7
                                               , ("Cheese", "Juice", "Milk"): 0.7}

        self.transactions_2 = [("Beef", "Chicken", "Milk"), ("Beef", "Cheese"), ("Cheese", "Boots"),
                               ("Beef", "Chicken", "Cheese"), ("Beef", "Chicken", "Clothes", "Cheese", "Milk"),
                               ("Chicken", "Clothes", "Milk"), ("Chicken", "Milk", "Clothes")]
        self.frequent_itemsets_dictionary_2 = {("Beef",): 4, ("Cheese",): 4, ("Chicken",): 5, ("Clothes",): 3,
                                               ("Milk",): 4
            , ("Beef", "Chicken"): 3, ("Beef", "Cheese"): 3, ("Chicken", "Clothes"): 3
            , ("Chicken", "Milk"): 4, ("Clothes", "Milk"): 3
            , ("Chicken", "Clothes", "Milk"): 3}
        self.expected_associate_rules_2 = {("Clothes",): ("Chicken",), ("Chicken",): ("Milk",)
            , ("Milk",): ("Chicken",), ("Clothes",): ("Milk",)
            , ("Milk",): ("Clothes"), ("Chicken", "Clothes"): ("Milk",)
            , ("Clothes", "Milk"): ("Chicken",)
            , ("Clothes",): ("Milk", "Chicken")}

        self.frequent_itemsets_sample = [(1, 2, 3), (1, 2, 4), (1, 3, 4), (1, 3, 5), (2, 3, 4)]
        self.expected_candidate_genenerate = [(1, 2, 3, 4)]

    def tearDown(self):
        self.transactions.clear()
        self.transactions = None

    def test__create_frequent_1_large_itemsets(self):
        # Arrange

        # Action
        result_dictionary = AprioriAlgorithm \
            .generate_frequent_1_large_itemsets(self.transactions, 0.5)

        # Assert
        # expected_dictionary = { (2,): 6, (3,): 4, (4,): 5}
        self.assertTrue(result_dictionary == self.frequent_1_large_itemsets)

    def test_candidate_generate(self):
        result = AprioriAlgorithm.candidate_generate(self.frequent_itemsets_sample)
        self.assertTrue(result == self.expected_candidate_genenerate)

    def test_create_itemsets_from_candidates(self):
        candidates = AprioriAlgorithm.candidate_generate(sorted(self.frequent_1_large_itemsets))
        result = AprioriAlgorithm.generate_frequent_itemsets(self.transactions, candidates, 0.5)
        self.assertTrue(result == {(2, 4): 4})

    def test_apriori_algorithm(self):
        result = AprioriAlgorithm.run(self.transactions, 0.5)
        self.assertTrue(result == {(2,): 6, (3,): 4, (4,): 5, (2, 4): 4})
        result_2 = AprioriAlgorithm.run(self.transactions_2, 0.3)

    def test_generate_associate_rules(self):
        result = AprioriAlgorithm.generate_associate_rules(self.frequent_itemsets_dictionary_2, 0.8, 3)
        #result_2 = AprioriAlgorithm.generate_associate_rules(self.frequent_itemsets_dictionary_2, 0.8, 1)
        self.assertTrue(result == self.expected_associate_rules_2)



test_suit = unittest.TestLoader().loadTestsFromTestCase(AprioriAlgorithmTests)
unittest.TextTestRunner().run(test_suit)
