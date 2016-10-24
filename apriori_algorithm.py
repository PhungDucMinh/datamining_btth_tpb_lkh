from math import ceil

from  frequent_itemsets_algorithm import IFrequentItemSetsAlgorithm
import itertools


class AprioriAlgorithm(IFrequentItemSetsAlgorithm):
    @staticmethod
    def run(transactions, minsup):
        all_frequent_itemsets = {}

        frequent_itemsets = AprioriAlgorithm.generate_frequent_1_large_itemsets(transactions, minsup)
        AprioriAlgorithm.__add_dictionary(all_frequent_itemsets, frequent_itemsets)

        while len(frequent_itemsets) > 0:
            candidates = AprioriAlgorithm.candidate_generate(sorted(frequent_itemsets))
            frequent_itemsets = AprioriAlgorithm.generate_frequent_itemsets(transactions, candidates, minsup)
            AprioriAlgorithm.__add_dictionary(all_frequent_itemsets, frequent_itemsets)

        return all_frequent_itemsets

    @staticmethod
    def __add_dictionary(dictonary1, dictionary2):
        for key, value in dictionary2.iteritems():
            dictonary1[key] = value

        return dictonary1

    @staticmethod
    def __generate_1_large_itemsets(transactions):
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
    def generate_frequent_1_large_itemsets(transactions, minsup):
        itemsets_dictionary = AprioriAlgorithm.__generate_1_large_itemsets(transactions)
        min_count = ceil(minsup * len(transactions))

        for key, value in itemsets_dictionary.items():
            if value < min_count:
                del itemsets_dictionary[key]

        return itemsets_dictionary

    @staticmethod
    def __candidate_generate_join_step(itemsets):
        # Convert each item in itemsets to tupple
        if not isinstance(itemsets[0], tuple):
            for index in range(len(itemsets)):
                itemsets[index] = tuple(itemsets[index])

        candidates = list()
        for index1, tupple1 in enumerate(itemsets):
            for index2, tupple2 in enumerate(itemsets):
                if index2 > index1:
                    # Check two sets different from last element
                    # If YES -> add to candidates
                    for index3 in range(len(tupple1)):
                        if index3 != (len(tupple1) - 1):
                            if tupple1[index3] != tupple2[index3]:
                                break
                        else:
                            if tupple1[index3] != tupple2[index3]:
                                candidates.append(tupple1 + (tupple2[len(tupple2) - 1],))
        return candidates

    @staticmethod
    def __candidate_generate_pruning_step(itemsets, candidates):
        for candidate in candidates:
            # Check any of "(k-1) candidate subsets" is not in itemsets F(k-1)
            # If YES -> Remove from candidates
            subsets = set(itertools.combinations(candidate, len(candidate) - 1))
            for subset in subsets:
                if not subset in itemsets:
                    candidates.remove(candidate)
                    break
        return candidates

    @staticmethod
    def candidate_generate(itemsets):
        generated_candidates = AprioriAlgorithm \
            .__candidate_generate_join_step(itemsets)
        return AprioriAlgorithm.__candidate_generate_pruning_step(itemsets, generated_candidates)

    @staticmethod
    def generate_frequent_itemsets(transactions, itemsets, minsup):
        itemsets_dictionary = AprioriAlgorithm.__generate_itemsets_dictionary(transactions, itemsets)
        min_count = ceil(minsup * len(transactions))

        for key, value in itemsets_dictionary.items():
            if value < min_count:
                del itemsets_dictionary[key]

        return itemsets_dictionary

    @staticmethod
    def __generate_itemsets_dictionary(transactions, itemsets):
        itemsets_dictionary = {}
        for transaction in transactions:
            for key in itemsets:
                if set(key).issubset(set(transaction)):
                    if not key in itemsets_dictionary:
                        itemsets_dictionary[key] = 1
                    else:
                        itemsets_dictionary[key] += 1

        return itemsets_dictionary

    @staticmethod
    def generate_result_content(frequent_items, transactions_size):
        content = ""
        keys  = sorted(frequent_items)
        for key in keys:
            content += str("{0:.2f}".format(float(frequent_items[key])/ transactions_size))
            for value in key:
                content += " " + str(value)
            content += "\n"
        return content
