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
    def __remove_itemsets_not_enough_support(transactions, itemsets_dictionary, minsup):
        min_count = ceil(minsup * len(transactions))

        for key, value in itemsets_dictionary.items():
            if value < min_count:
                del itemsets_dictionary[key]

        return itemsets_dictionary

    @staticmethod
    def generate_frequent_1_large_itemsets(transactions, minsup):
        itemsets_dictionary = AprioriAlgorithm.__generate_1_large_itemsets(transactions)
        return AprioriAlgorithm.__remove_itemsets_not_enough_support(transactions, itemsets_dictionary, minsup)

    @staticmethod
    def __candidate_generate_join_step(itemsets):
        # Convert each item in itemsets to tupple

        # if not isinstance(itemsets[0], tuple):
        #     for index in range(len(itemsets)):
        #         itemsets[index] = tuple(itemsets[index])

        candidates = list()
        for index1, itemset1 in enumerate(itemsets):
            for index2, itemset2 in enumerate(itemsets):
                if index2 > index1:
                    # Check two sets different from last element
                    # If YES -> add to candidates
                    for index3 in range(len(itemset1)):
                        if index3 != (len(itemset1) - 1):
                            if itemset1[index3] != itemset2[index3]:
                                break
                        else:
                            if itemset1[index3] != itemset2[index3]:
                                candidates.append(itemset1 + (itemset2[len(itemset2) - 1],))
                                #candidates.append(frozenset(itemset1 + itemset2))
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
    def generate_frequent_itemsets(transactions, candidates, minsup):
        itemsets_dictionary = AprioriAlgorithm.__generate_itemsets_dictionary(transactions, candidates)
        return AprioriAlgorithm.__remove_itemsets_not_enough_support(transactions, itemsets_dictionary, minsup)

    @staticmethod
    def __generate_itemsets_dictionary(transactions, candidates):
        """
        This function is slow, need to be update 24/11 11h30
        :param transactions: transaction list
        :param candidates: F (k-1) itemsets
        :return: dictionary<key,value> where key is tupple(items), value = support.count
        """
        itemsets_dictionary = {}

        for transaction in transactions:
            for candidate in candidates:
                # This is the slow method => update soon :v
                if frozenset(candidate).issubset(transaction):
                    if not itemsets_dictionary.has_key(candidate):
                        itemsets_dictionary[candidate] = 1
                    else:
                        itemsets_dictionary[candidate] += 1
        return itemsets_dictionary

    @staticmethod
    def generate_result_content(frequent_items, transactions_size):
        content = ""
        keys = sorted(frequent_items)
        for key in keys:
            content += str("{0:.2f}".format(float(frequent_items[key]) / transactions_size))
            for value in key:
                content += " " + str(value)
            content += "\n"
        return content
