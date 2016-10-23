import  re
class ReadData:

    @staticmethod
    def read_as_number(file_name, mode):
        """
        Read file according file name and open mode
        Return type = list<list<number>>
        """
        file = open(file_name, mode)
        content = file.readlines()
        transactions = list()
        for line in content:
            # List of string_number
            string_of_numbers = filter(None, re.split(" |\n", line))
            numbers = list()
            # Make list of string_number become list of number
            for string_number in string_of_numbers:
                numbers.append( int(string_number))
            # Add to transaction
            transactions.append(numbers)
        file.close()
        return transactions


    @staticmethod
    def read_as_string(file_name, mode):
        """
        Read file according file name and open mode
        Return type = list<list<number>>
        """
        file = open(file_name, mode)
        content = file.readlines()
        transactions = list()
        for line in content:
            # List of string_number
            string_of_numbers = filter(None, re.split(" |\n", line))
            transactions.append(string_of_numbers)
        file.close()
        return transactions

data = ReadData.read_as_number("retail.dat", "r")
data2 = ReadData.read_as_string("retail.dat", "r")