Day 3
Topics
classes
self
methods
__init__
subclassing
modules
nested comp
Refer
https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions
https://docs.python.org/3/tutorial/modules.html
https://docs.python.org/3/tutorial/classes.html
https://www.youtube.com/watch?v=8moWQ1561FY - OOP explained by Raymond
Practice
dictionaries

given a list of numbers (nums = [1, 2, 3]) use dict comprehension to create a dict of squares { 1: 1, 2: 4, 3: 9}
make a list of values alone from the above dictionary [1, 4, 9] using list comprehension
set comprehension

given a list [1, 2, 5, 2, 3, 1, 4, 5], create squares of unique items using set comprehension. {1, 4, 9, 16, 25}
Given a list of tuples with current and min balances: [("Guido", 2000, 500), ("Raymond", -52, 1000), ("Jack", 900, 1000), ("Brandon", 2000, 0)] use comprehensions to get the below:

dict of those with proper balances (above or equal min bal) {"Guido": 2000, "Brandon": 2000}
set of all balances {2000, -52, 900}
list of account holders ["Guido", "Raymond", "Jack", "Brandon"]
dict of user and money each need to fulfill the min balance requirement (those who already have enough bal should not be in the dict) {"Raymond": 1052, "Jack": 100}
list of tuples with name and current balance if the balance is above 0 [("Guide", 2000), ("Jack", 900), ("Brandon", 2000)]
Write a Developer class that has a code function and a languages list.

code function should accept a language param and if the language is in the languages list it should print code in <language>.
resume function that prints languages of the developer.
Write a SrDeveloper class that inherits Developer and adds review function. review should also be limited to languages list.
Write a TechLead class that inherits from SrDeveloper and adds design function
create a class that provides the factorials for the list of numbers provided.

import a func from a module and call it to print some output

import a func and rename it to use in your module from another

create a module that prints "I'm running" only when it's ran as a script (not as a module using import)

use python to open another python source file and print the contents

Extra Mile
Checkout __repr__ and __str__ methods and implement those for your class
see what other dunder methods interest you and let me know your fav
