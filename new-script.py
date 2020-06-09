#!/bin/python3
import sys #system functions and parameters
from datetime import datetime as dt #import with alias
print(sys.version)
print(dt.now())

my_name = "Edward"
print(my_name[0])
print(my_name[-1])

sentence = "This is a sentence."
print(sentence[:4])

print(sentence.split())

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)

quote = "He said, 'give me the cash'"
print(quote)

quote = "He said, \"give me the cash\""
print(quote)

too_much_space = "              hello          "
print(too_much_space.strip())

print("a" in "Apple")

letter = "A"
word = "Apple"
print(letter.lower() in word.lower()) #improved

movie = "The Matrix"
print("My favorite movie is {}.".format(movie))

#Dictionaries - key/value pairs {}
drinks = {"beer": 7, "wine":5, "butts":9} #drink is key, price is value
print(drinks)

employees = {"Finance": ["Bob", "Linda", "Tina"], "IT": ["Gene", "Louise", "Teddy"], "HR": ["Jimmy Jr", "Mort"]}
print(employees)

employees['Legal'] = ["Mr. Frond"] #add new key:value pair
print(employees)

employees.update({"Sales": ["Andie", "Ollie"]})
print(employees)

drinks["beer"] = 2
print(drinks)

print(drinks.get("beer"))

