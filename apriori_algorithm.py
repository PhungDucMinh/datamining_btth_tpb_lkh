from  frequent_itemsets_algorithm import IFrequentItemSetsAlgorithm


class AprioriAlgorithm(IFrequentItemSetsAlgorithm):
    def run(self, dict, minsup):
        raise NotImplementedError

    def determine_set_of_frequent_1_itemsets(self):
        raise NotImplementedError


class AprioriItem:
    __item = None
    __support = 0

    def __init__(self, item):
        self.__item = item
        self.__support = 0

    def __init__(self, item, support):
        self.__item = item
        self.__support = support

    def get_support(self):
        return self.__support

    def add_support(self):
        self.__support += 1

    def substract_support(self):
        if self.__support > 0:
            self.__support -= 1

    def get_item(self):
        return self.__item


class AprioriItemSet:
    __items = []

    def __init__(self):
        self.__items = list()

    # Add item if item is not in set
    # Add item support if item in set
    def add_item(self, item):
        if not isinstance(item, AprioriItem):
            raise TypeError("Need AprioriItem type")

        if item in self.__items:
            raise ValueError("Item is in the Set, can't add")

        if item not in self.__items:
            self.__items.append(item)

    def add_item_support(self, item):
        if not isinstance(item, AprioriItem):
            raise TypeError("Need AprioriItem type")

        if item not in self.__items:
            raise ValueError("Item is not in Set, can't add support")

        index = self.__items.index(item)
        AprioriItem(self.__items[index]).add_support()

    def remove_item(self, item):
        if not isinstance(item, AprioriItem):
            raise TypeError("Need AprioriItem type")

        if item not in self.__items:
            raise ValueError("Item is not in Set, can't remove item")
        else:
            self.__items.remove(item)

    def substract_item_support(self, item):
        if not isinstance(item, AprioriItem):
            raise TypeError("Need AprioriItem type")

        if item not in self.__items:
            raise ValueError("Item is not in Set, can't remove item")
        else:
            index = self.__items.index(item)
            AprioriItem(self.__items[index]).substract_support()

    def has_item(self, item):
        return True

    def __contains__(self, item):
        return item in self.__items
