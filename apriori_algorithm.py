from math import ceil

from  frequent_itemsets_algorithm import IFrequentItemSetsAlgorithm
import itertools


class AprioriAlgorithm(IFrequentItemSetsAlgorithm):

    @staticmethod
    def run(transactions, minsup):
        all_frequent_itemsets = {}
        frequent_itemsets = AprioriAlgorithm.create_frequent_1_large_itemsets(transactions,minsup)
        for key,value in frequent_itemsets.iteritems():
            all_frequent_itemsets[key] = value
        while len(frequent_itemsets) > 0:
            candidates = AprioriAlgorithm.candidate_generate(sorted(frequent_itemsets))
            frequent_itemsets = AprioriAlgorithm.create_frequent_itemsets(transactions,candidates, minsup)
            for key,value in frequent_itemsets.iteritems():
                all_frequent_itemsets[key] = value
        return all_frequent_itemsets

    @staticmethod
    def create_1_large_itemsets(transactions):
        itemsets = {}
        for transaction in transactions:
            for item in transaction:
                key = (item,)
                if not key in itemsets:
                    itemsets[key] = 1
                else:
                    itemsets[key] += 1

        return itemsets

    @staticmethod
    def create_frequent_1_large_itemsets(transactions, minsup):
        itemsets_dictionary = AprioriAlgorithm.create_1_large_itemsets(transactions)
        min_count = ceil(minsup * len(transactions))

        for key, value in itemsets_dictionary.items():
            if value < min_count:
                del itemsets_dictionary[key]

        return itemsets_dictionary

    @staticmethod
    def candidate_generate_join_step(itemsets):
        # Convert each item in itemsets to tupple
        if not isinstance(itemsets[0],tuple):
            for index in range(len(itemsets)):
                itemsets[index] = tuple(itemsets[index])

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

    @staticmethod
    def candidate_generate_pruning_step(itemsets, generated_candidates):
        #accepted_itemsets_list = list()
        for candidate in generated_candidates:
            subsets = set(itertools.combinations(candidate, len(candidate) - 1))
            for subset in subsets:
                if not subset in itemsets:
                    generated_candidates.remove(candidate)
                    break
        return generated_candidates

    @staticmethod
    def candidate_generate(itemsets):
        generated_candidates = AprioriAlgorithm\
            .candidate_generate_join_step(itemsets)
        return AprioriAlgorithm.candidate_generate_pruning_step(itemsets, generated_candidates)

    @staticmethod
    def create_frequent_itemsets(transactions, itemsets, minsup):
        itemsets_dictionary = AprioriAlgorithm.create_itemsets_dictionary(transactions, itemsets)
        min_count = ceil(minsup * len(transactions))

        for key, value in itemsets_dictionary.items():
            if value < min_count:
                del itemsets_dictionary[key]

        return itemsets_dictionary

    @staticmethod
    def create_itemsets_dictionary(transactions, itemsets):
        itemsets_dictionary = {}
        for transaction in transactions:
            for key in itemsets:
                if set(key).issubset(set(transaction)):
                    if not key in itemsets_dictionary:
                        itemsets_dictionary[key] = 1
                    else:
                        itemsets_dictionary[key] += 1

        return itemsets_dictionary