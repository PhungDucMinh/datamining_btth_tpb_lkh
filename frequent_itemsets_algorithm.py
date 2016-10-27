import itertools


class IFrequentItemSetsAlgorithm:
    def run(self, dict, minsup):
        raise NotImplementedError

    @staticmethod
    def generate_associate_rules(frequent_itemsets_dictionary, minconf, itemset_len):
        if itemset_len <=0:
            raise ValueError("k must be bigger than 0")

        if minconf > 1 or minconf <0:
            raise ValueError("minconf must be in [0;1]")

        if itemset_len == 1:
            keys_sort_with_len = sorted(frequent_itemsets_dictionary.keys(), key=len, reverse=True)
            max_len = len(keys_sort_with_len[0])
            full_associate_rules = {}
            for i in range(2,max_len + 1):
                for key, value in IFrequentItemSetsAlgorithm.generate_associate_rules(frequent_itemsets_dictionary, minconf, i).iteritems():
                    full_associate_rules[key] = value
            return  full_associate_rules

        return IFrequentItemSetsAlgorithm.generate_associate_rules_specify_itemset_len(frequent_itemsets_dictionary, minconf, itemset_len)

    @staticmethod
    def generate_associate_rules_specify_itemset_len(frequent_itemsets_dictionary, minconf, itemset_len):
        frequent_k_large_itemsets_dictionary = IFrequentItemSetsAlgorithm \
            .__generate_frequent_k_itemsets(frequent_itemsets_dictionary, itemset_len)
        association_rules = {}
        right_side_itemsets = []

        for key, value in frequent_k_large_itemsets_dictionary.iteritems():
            for item in key:
                right_side_itemset = (item,)
                left_side_itemset = tuple(sorted(set(key) - set(right_side_itemset)))
                conf = float(frequent_itemsets_dictionary[key]) / frequent_itemsets_dictionary[left_side_itemset]
                if conf >= minconf:
                    new_key = (left_side_itemset, right_side_itemset)
                    association_rules[new_key] = conf
                    right_side_itemsets.append(right_side_itemset)

            IFrequentItemSetsAlgorithm.__ap_generate_rules \
                (frequent_itemsets_dictionary, minconf, key, association_rules, right_side_itemsets, 1)
        return association_rules

    @staticmethod
    def associate_rules_to_string(associate_rules):
        content = ""
        for key in sorted(associate_rules):
            value = associate_rules[key]
            content += "{0:.2f}".format(value)
            for item in key[0]:
                content += " " + str(item)
            content += " ->"
            for item in key[1]:
                content += " " + str(item)
            content += "\n"
        return content

    @staticmethod
    def __generate_frequent_k_itemsets(frequent_itemsets_dictionary, k):
        frequent__k_large_itemsets_dictionary = {}
        for key, value in frequent_itemsets_dictionary.iteritems():
            if len(key) == k:
                frequent__k_large_itemsets_dictionary[key] = value
        return frequent__k_large_itemsets_dictionary

    @staticmethod
    def __ap_generate_rules(frequent_itemsets_dictionary, minconf, itemset, associate_rules, pre_candidates, m):
        candidates = []
        if len(itemset) > m + 1 and len(associate_rules) != 0:
            for x in IFrequentItemSetsAlgorithm.candidate_generate(pre_candidates):
                candidates.append(x)
            for candidate in candidates:
                f_alpha_itemset = tuple(sorted(set(itemset) - set(candidate)))
                conf = float(frequent_itemsets_dictionary[itemset]) / frequent_itemsets_dictionary[f_alpha_itemset]
                if conf >= minconf:
                    key = (tuple(sorted(set(itemset) - set(candidate))), candidate)
                    associate_rules[key] = conf
                else:
                    candidates.remove(candidate)
            IFrequentItemSetsAlgorithm.__ap_generate_rules(frequent_itemsets_dictionary, minconf, itemset,
                                                           associate_rules, candidates, m + 1)

    @staticmethod
    def candidate_generate(itemsets):
        generated_candidates = IFrequentItemSetsAlgorithm \
            .__candidate_generate_join_step(itemsets)
        return IFrequentItemSetsAlgorithm.__candidate_generate_pruning_step(itemsets, generated_candidates)

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
                                # candidates.append(frozenset(itemset1 + itemset2))
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
