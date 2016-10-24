import re


class FileIO:
    @staticmethod
    def read(file_name, mode, func):
        file = open(file_name, mode)
        content = file.readlines()
        transactions = list()
        for line in content:
            transactions.append(func(line))
        file.close()
        return transactions

    @staticmethod
    def read_as_number_list_type(file_name, mode):
        return FileIO.read(file_name, mode, FileIO.as_number_list())

    @staticmethod
    def as_number_list(line):
        # List of string_number
        string_of_numbers = filter(None, re.split(" |\n", line))
        numbers = list()
        # Make list of string_number become list of number
        for string_number in string_of_numbers:
            numbers.append(int(string_number))
        return numbers

    @staticmethod
    def read_as_string_list_type(file_name, mode):
        return FileIO.read(file_name, mode, FileIO.as_string_list)

    @staticmethod
    def as_string_list(line):
        # List of string_number
        return filter(None, re.split(" |\n", line))

    @staticmethod
    def read_as_string_tupple_type(file_name, mode):
        return FileIO.read(file_name, mode, FileIO.as_string_tupple)

    @staticmethod
    def as_string_tupple(line):
        # List of string_number
        return tuple(filter(None, re.split(" |\n", line)))

    @staticmethod
    def read_as_number_tupple_type(file_name, mode):
        return FileIO.read(file_name, mode, FileIO.as_number_tupple)

    @staticmethod
    def as_number_tupple(line):
        # List of string_number
        string_of_numbers = filter(None, re.split(" |\n", line))
        numbers = list()
        # Make list of string_number become list of number
        for string_number in string_of_numbers:
            numbers.append(int(string_number))
        # Add to transaction
        return tuple(numbers)


"""
data = ReadData.read_as_number_list_type("retail.dat", "r")
data2 = ReadData.read_as_string_tupple_type("retail.dat", "r")
print data2
"""
