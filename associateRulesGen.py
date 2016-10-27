from frequent_itemsets_algorithm import IFrequentItemSetsAlgorithm
from fileIO import FileIO
import sys

input_file_name = str(sys.argv[1])
output_file_name = str(sys.argv[2])
minconf = float(sys.argv[3])
k = int(sys.argv[4])

frequent_itemsets_dict = FileIO.read_frequent_itemsets(input_file_name, "r")
result = IFrequentItemSetsAlgorithm.generate_associate_rules(frequent_itemsets_dict, minconf, k)
content = IFrequentItemSetsAlgorithm.associate_rules_to_string(result)
print content
FileIO.write(output_file_name, "w", content)

"""
frequent_itemsets_dict = FileIO.read_frequent_itemsets("retail_out.txt", "r")
result = IFrequentItemSetsAlgorithm.generate_associate_rules(frequent_itemsets_dict, 0.4, 1)
content = IFrequentItemSetsAlgorithm.associate_rules_to_string(result)
print content
FileIO.write("associate_rules_out.txt", "w", content)
"""