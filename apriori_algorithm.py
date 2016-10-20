from  frequent_itemsets_algorithm import IFrequentItemSetsAlgorithm


class AprioriAlgorithm(IFrequentItemSetsAlgorithm):
    def run(self, dict, minsup):
        raise NotImplementedError

    def create_frequent_1_item_set(self, transaction_list):
        item_set_dictionary = {}

        for transaction in transaction_list:
            for item in transaction:
                if not item_set_dictionary.has_key(item):
                    item_set_dictionary[item] = 1
                else:
                    item_set_dictionary[item] += 1

        return item_set_dictionary
