# Write a function that will find all the anagrams of a word from a list.
# You will be given two inputs a word and an array with words. You should
# return an array of all the anagrams or an empty array if there are none.

# a = 'abba'
# c =  ['aabb', 'abcd', 'bbaa', 'dada']
# print([i for i in c if sorted(i) == sorted(a)])


# You are given an array of strings that need to be spread among N columns.
# Each column's width should be the same as the length of the longest string inside it.
# Separate columns with " | ", and lines with "\n"; content should be left-justified.


a = {"1", "12", "123", "1234", "12345", "123456"}
list = list(sorted(a))


print([list[i::3] for i in range(3)])


# print(math.ceil(7/3))


