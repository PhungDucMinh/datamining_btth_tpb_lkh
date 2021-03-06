import re


class FileIO:
    @staticmethod
    def __read(file_name, mode, func):
        file = open(file_name, mode)
        content = file.readlines()
        transactions = list()
        for line in content:
            transactions.append(func(line))
        file.close()
        return transactions

    @staticmethod
    def read_as_number_list_type(file_name, mode):
        return FileIO.__read(file_name, mode, FileIO.__as_number_list)

    @staticmethod
    def __as_number_list(line):
        # List of string_number
        string_of_numbers = filter(None, re.split(" |\n", line))
        numbers = list()
        # Make list of string_number become list of number
        for string_number in string_of_numbers:
            numbers.append(int(string_number))
        return numbers

    @staticmethod
    def read_as_string_list_type(file_name, mode):
        return FileIO.__read(file_name, mode, FileIO.__as_string_list)

    @staticmethod
    def __as_string_list(line):
        # List of string_number
        return filter(None, re.split(" |\n", line))

    @staticmethod
    def read_as_string_tupple_type(file_name, mode):
        return FileIO.__read(file_name, mode, FileIO.__as_string_tupple)

    @staticmethod
    def __as_string_tupple(line):
        # List of string_number
        return tuple(filter(None, re.split(" |\n", line)))

    @staticmethod
    def read_as_number_tupple_type(file_name, mode):
        return FileIO.__read(file_name, mode, FileIO.__as_number_tupple)

    @staticmethod
    def __as_number_tupple(line):
        # List of string_number
        string_of_numbers = filter(None, re.split(" |\n", line))
        numbers = list()
        # Make list of string_number become list of number
        for string_number in string_of_numbers:
            numbers.append(int(string_number))
        # Add to transaction
        return tuple(numbers)

    @staticmethod
    def write(file_name, mode, content):
        file_output = open(file_name, mode)
        file_output.write(content)
        file_output.close()


    @staticmethod
    def read_as_frozensets(file_name, mode):
        return FileIO.__read(file_name, mode, FileIO.__as_frozensets)

    @staticmethod
    def __as_frozensets(line):
        string_of_numbers = filter(None, re.split(" |\n", line))
        numbers = list()
        # Make list of string_number become list of number
        for string_number in string_of_numbers:
            numbers.append(int(string_number))
        # Add to transaction
        return frozenset(numbers)

    @staticmethod
    def read_frequent_itemsets(file_name, mode):
        file = open(file_name,mode)
        lines = file.readlines()

        frequent_itemset_dict = {}
        for line in lines:
            strs = filter(None, re.split(" |\n", line))
            value = float(strs.pop(0))
            numbers = []
            for item in strs:
                numbers.append(int(item))
            key = tuple(sorted(numbers))
            frequent_itemset_dict[key] = value
        return frequent_itemset_dict

"""
data = ReadData.read_as_number_list_type("retail.dat", "r")
data2 = ReadData.read_as_string_tupple_type("retail.dat", "r")
print data2
"""
