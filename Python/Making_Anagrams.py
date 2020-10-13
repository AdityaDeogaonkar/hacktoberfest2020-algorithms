'''Program to count the minimum number of deletions required to make 2 strings anagrams
    For eg:
    string1 = abcdefg
    string2 = abcd
    Output = 3
    as deleting 'efg' will make string1 and string2 anagrams'''

from collections import Counter
def makingAnagrams(s1, s2):
    return len(s1)+len(s2)-sum((Counter(s1) & Counter(s2)).values())*2

a = input() 
b = input() 
print(makingAnagrams(a,b))
