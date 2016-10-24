from fileIO import FileIO
from apriori_algorithm import AprioriAlgorithm
transaction = FileIO.read_as_number_list_type("retail.dat", "r")
result = AprioriAlgorithm.run(transaction, 0.3)
print result
print AprioriAlgorithm.generate_result_content(result, len(transaction))