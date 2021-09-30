# Write a function that will find all the anagrams of a word from a list.
# You will be given two inputs a word and an array with words. You should
# return an array of all the anagrams or an empty array if there are none.

a = 'abba'
c =  ['aabb', 'abcd', 'bbaa', 'dada']
print([i for i in c if sorted(i) == sorted(a)])
