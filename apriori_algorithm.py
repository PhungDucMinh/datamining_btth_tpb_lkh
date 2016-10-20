from math import ceil

from  frequent_itemsets_algorithm import IFrequentItemSetsAlgorithm


class AprioriAlgorithm(IFrequentItemSetsAlgorithm):
    def run(self, dict, minsup):
        raise NotImplementedError

    def create_1_item_set(self, transaction_list):
        item_set_dictionary = {}

        for transaction in transaction_list:
            for item in transaction:
                if not item in item_set_dictionary:
                    item_set_dictionary[item] = 1
                else:
                    item_set_dictionary[item] += 1

        return item_set_dictionary

    def create_frequent_1_item_set(self, transaction_list, minsup):
        item_set_dictionary = self.create_1_item_set(transaction_list)
        min_count = ceil(minsup * len(transaction_list))

        for key, value in item_set_dictionary.items():
            if value < min_count:
                del item_set_dictionary[key]

        return item_set_dictionary
