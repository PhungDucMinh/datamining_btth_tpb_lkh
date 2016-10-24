from fileIO import FileIO
from apriori_algorithm import AprioriAlgorithm
import sys

minsup = float(sys.argv[3])
input_file = sys.argv[1]
output_file = sys.argv[2]
transaction = FileIO.read_as_number_tupple_type(input_file, "r")
#transaction = FileIO.read_as_number_list_type("retail.dat", "r")
result = AprioriAlgorithm.run(transaction, minsup)
content = AprioriAlgorithm.generate_result_content(result, len(transaction))
FileIO.write(output_file, "w", content)
print content