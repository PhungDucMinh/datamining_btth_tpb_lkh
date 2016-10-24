from math import ceil

from  frequent_itemsets_algorithm import IFrequentItemSetsAlgorithm


class AprioriAlgorithm(IFrequentItemSetsAlgorithm):
    def run(self, dict, minsup):
        raise NotImplementedError

    def create_1_item_set(self, transaction):
        item_set_dictionary = {}

        for transaction in transaction:
            for item in transaction:
                key = str((item))
                if not key in item_set_dictionary:
                    item_set_dictionary[key] = 1
                else:
                    item_set_dictionary[key] += 1

        return item_set_dictionary

    def create_frequent_1_item_set(self, transactions, minsup):
        item_set_dictionary = self.create_1_item_set(transactions)
        min_count = ceil(minsup * len(transactions))

        for key, value in item_set_dictionary.items():
            if value < min_count:
                del item_set_dictionary[key]

        return item_set_dictionary

    @staticmethod
    def candidate_generate_join_step(itemsets):
        generated_candidates = list()
        for index1, tupple1 in enumerate(itemsets):
            for index2, tupple2 in enumerate(itemsets):
                if index2 > index1:
                    # Two sets differ last element
                    for index3 in range(len(tupple1)):
                        if index3 != (len(tupple1) - 1):
                            if tupple1[index3] != tupple2[index3]:
                                break
                        else:
                            if tupple1[index3] != tupple2[index3]:
                                generated_candidates.append(tupple1 + (tupple2[len(tupple2) - 1],))
        return generated_candidates

    # Implement here!
    @staticmethod
    def candidate_generate_pruning_step(itemsets, generated_candidates):
        #accepted_itemsets_list = list()
        for candidate in generated_candidates:
            delete = True
            for itemset in itemsets:
                if set(itemset).issubset(set(candidate)):
                    delete = False
                    break
            if delete:
                generated_candidates.remove(candidate)
        return generated_candidates

    @staticmethod
    def candidate_generate(itemsets):
        generated_candidates = AprioriAlgorithm\
            .candidate_generate_join_step(itemsets)
        return AprioriAlgorithm.candidate_generate_pruning_step(itemsets, generated_candidates)
