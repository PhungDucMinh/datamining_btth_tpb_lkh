from fileIO import FileIO
from apriori_algorithm import AprioriAlgorithm
import time

start_time = time.time()

transaction = FileIO.read_as_frozensets("retail.dat", "r")

print ("Read file time: {0:.3f}s".format(time.time() - start_time))
start_time = time.time()

result = AprioriAlgorithm.run(transaction, 0.02)

print AprioriAlgorithm.generate_result_content(result, len(transaction))

print ("Read file time: {0:.3f}s".format(time.time() - start_time))