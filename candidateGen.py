from apriori_algorithm import AprioriAlgorithm

input1 = [ (1, ), (2,), (3,), (4,)]
input2 = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
input3 = [(1,2,3), (1,2,4), (1,3,4), (1,3,5), (2,3,4)]
#output1 = AprioriAlgorithm.candidate_generate_join_step(input1)
#output2 = AprioriAlgorithm.candidate_generate_join_step(input2)
result = AprioriAlgorithm.candidate_generate(input3)
#print output1
#print output2
print result