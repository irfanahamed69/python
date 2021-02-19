"""given a list of numbers (nums = [1, 2, 3]) use dict comprehension to create a dict of squares { 1: 1, 2: 4, 3: 9}
make a list of values alone from the above dictionary [1, 4, 9] using list comprehension"""
nums = [1, 2, 3]
dictcomp = {x : pow(x,2) for x in nums }
print(dictcomp)
lis = [y for y in dictcomp.values()]
print(lis)

"""given a list [1, 2, 5, 2, 3, 1, 4, 5], create squares of unique items using set comprehension. {1, 4, 9, 16, 25}"""
nums = [1, 2, 5, 2, 3, 1, 4, 5]
setcomp = {pow(x,2) for x in nums }
print(setcomp)

"""Given a list of tuples with current and min balances: [("Guido", 2000, 500), ("Raymond", -52, 1000), ("Jack", 900, 1000), ("Brandon", 2000, 0)] use comprehensions to get the below:

dict of those with proper balances (above or equal min bal) {"Guido": 2000, "Brandon": 2000}
set of all balances {2000, -52, 900}
list of account holders ["Guido", "Raymond", "Jack", "Brandon"]
dict of user and money each need to fulfill the min balance requirement (those who already have enough bal should not be in the dict) {"Raymond": 1052, "Jack": 100}
list of tuples with name and current balance if the balance is above 0 [("Guide", 2000), ("Jack", 900), ("Brandon", 2000)]"""

listTup = [("Guido", 2000, 500), ("Raymond", -52, 1000), ("Jack", 900, 1000), ("Brandon", 2000, 0)]

dict = {x[0] : x[1] for x in listTup if x[1] > x[2] }
print(dict)

sets = {x[1] for x in listTup}
print(sets)

Li = [x[0] for x in listTup ]
print(Li)

dict1 = {x[0]: x[2] - x[1] for x in listTup if x[2] > x[1]}
print(dict1)

listup = [x[0:2] for x in listTup if x[1] > 0]
print(listup)

#create a class that provides the factorials for the list of numbers provided.
class factorial:

    def fact(lis):
      for item in lis:
        facts = 1
        for num in (range(1, item + 1)):
          facts = facts * num
        print('The factorial of ',item,' is ',facts)
       

print(factorial.fact([1,2,3]))

##Developer,SrDeveloper,TechLead, repr(debugging),str(userfriendly)

class Developer:
    def __init__(self):
        self.languages = []

    def code(self, lang):
        if lang in self.languages:
            return str('Code in '+ lang)
        else:
            return str('Code '+lang+' not supported')

    def resume(self):
        return (self.languages)

    def __repr__(self):
        return str(Developer) 

    def __str__(self):
        return str(Developer) 

class SrDeveloper(Developer):
    def __init__(self):
      Developer.__init__(self)

    def review(self,lang):
        self.languages.append(lang)
        return (self.languages)

    def __repr__(self):
        return str(Developer) 

    def __str__(self):
        return str(Developer) 

class TechLead(SrDeveloper):
    def __init__(self):
      SrDeveloper.__init__(self)

    def design(self,lang):
        self.languages.append(lang)
        return (self.languages)

    def __repr__(self):
        return str(TechLead) 

    def __str__(self):
        return str(TechLead) 
    
x = TechLead()
print(x.review('python'))
print(x.design('java'))
print(x.code('C'))
print(repr(x))
print(str(x))
print(str(x.languages))
print(repr(x.languages))

# import a func from a module and call it to print some output

#main.py
from addition import  add

print(add(5,5))

#addition.py
def add(a,b):
  return a + b

#import a func and rename it to use in your module from another  
#main.py
from addition import  add as addNum

print(addNum(5,5))

#addition.py
def add(a,b):
  return a + b
  
#create a module that prints "I'm running" only when it's ran as a script (not as a module using import)
 
#main.py
import Hello

if __name__ == '__main__':
    print(__name__,' is running')
else:
    print(__name__,' is running')
    
#Hello.py
if __name__ == '__main__':
   print(__name__,'is running')
else :
  print(__name__,'is running')
  
##use python to open another python source file and print the contents
with open('Hello.py','r') as content:
  print (content.read()) 
