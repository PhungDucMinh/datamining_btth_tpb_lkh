dictionary = { (1,2,3): 10, (1,3,4): 6, (1,2,4) : 7}
for key,value in sorted(dictionary.iteritems()):
    print key,value
