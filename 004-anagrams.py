#Anagrams are the words that are formed by similar elements 
# but the orders in which these characters occur differ.

from collections import defaultdict
test_list = ['lump', 'eat',  'me',  'tea', 'em', 'plum']

temp = defaultdict(list)

for ele in test_list:
    temp[str(sorted(ele))].append(ele)
res = list(temp.values())
# print result
print("The grouped Anagrams : " + str(res))

##---------------------------------
# Python3 code to demonstrate
# Grouping Anagrams
# using list comprehension + sorted() + lambda + groupby()
from itertools import groupby
test_list = ['lump', 'eat',  'me',  'tea', 'em', 'plum']

key = lambda ulsorted_list:sorted(ulsorted_list)
res = [list(v) for k , v in groupby(sorted(test_list,key=key), key)]
# print result
print("The grouped Anagrams : " + str(res))

