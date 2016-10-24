from apriori_algorithm import AprioriAlgorithm
from read_file import FileIO

import sys

file_name = "candidateGen_input.txt"
#itemsets = FileIO.read_as_string_tupple_type(file_name, "r")
itemsets = FileIO.read_as_number_tupple_type(file_name, "r",)
result = AprioriAlgorithm.candidate_generate(itemsets)

print result