import pytest
list1 = [2,6,-7,12]
list2 = [33,17,19,24,66,144,22]
num = min(len(list1), len(list2))
result = [None]*(num*2)
result[::2] = list1[:num]
result[1::2] = list2[:num]
result.extend(list1[num:])
result.extend(list2[num:])
result
print (result)pyte