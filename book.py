'''
a program to show how to read from file and use re and collections library
'''

import re
import collections
# take content of book.txt, make it lower case and pass it to the book varialbe
text = open("book.txt").read().lower()
'''
using the findall function of the re library to search text
for words (\w+ is a reg expression for this)
'''
words = re.findall('\w+', text)

'''
using collections library to count the occurances of different
words in the words variable and to display the ten most common words
'''
print (collections.Counter(words).most_common(10))