from math import ceil

from  frequent_itemsets_algorithm import IFrequentItemSetsAlgorithm


class AprioriAlgorithm(IFrequentItemSetsAlgorithm):
    def run(self, dict, minsup):
        raise NotImplementedError

    def create_1_item_set(self, transaction_list):
        item_set_dictionary = {}

        for transaction in transaction_list:
            for item in transaction:
                key = str((item))
                if not key in item_set_dictionary:
                    item_set_dictionary[key] = 1
                else:
                    item_set_dictionary[key] += 1

        return item_set_dictionary

    def create_frequent_1_item_set(self, transaction_list, minsup):
        item_set_dictionary = self.create_1_item_set(transaction_list)
        min_count = ceil(minsup * len(transaction_list))

        for key, value in item_set_dictionary.items():
            if value < min_count:
                del item_set_dictionary[key]

        return item_set_dictionary

    @staticmethod
    def candidate_generate_join_step(itemsets_list):
        generated_itemsets_list = list()
        for index1, tupple1 in enumerate(itemsets_list):
            for index2, tupple2 in enumerate(itemsets_list):
                if index2 > index1:
                    # Two sets differ last element
                    if tupple1[len(tupple1) - 1] != tupple2[len(tupple2) - 1]:
                        generated_itemsets_list.append(tupple1 + (tupple2[len(tupple2) - 1],))
        return generated_itemsets_list

    # Implement here!
    def candidate_generate_pruning_step(self, dictionary):
        pass
