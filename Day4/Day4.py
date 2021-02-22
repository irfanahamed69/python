#Exercise 1

class jumper:

    def __init__(self,data):
        self.data = data
        self.index = 0


    def __iter__(self):
         return self

    def __next__(self):
        if len(self.data) <= self.index:
            raise StopIteration
        self.output = self.data[self.index]
        self.index = self.index + 2
        return self.output
        
j = jumper('hello')
it = iter(j)
print(next(it))
print(next(it))
print(next(it))
print(next(it))     

""" k = jumper('python')
it = iter(k)
print(next(it))
print(next(it))
print(next(it))
print(next(it)) """ 

#Exercise 2

import csv

header = ['name','experience']
rows = [['abc',5],['def',4],['ghi',3]]
with open('emp.csv','w',newline = '') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(header)
    for x in range(len(rows))  :
        csvwriter.writerow(rows[x])
        
#Exercise 3

import os
current_dir = os.getcwd()
for root, dirs,files in os.walk(current_dir):
   for file in files:
       if file.endswith('.py'):
            print(os.path.join(root,file))
            
#Exercise 4

import sys

n = len(sys.argv)

print('Total length of arguments',n)
print('First arggument will always be module name',sys.argv[0])

for i in range(1,n):
   print(i, 'argument is', sys.argv[i])
def addition(a,b):
   return a+b

print(addition(5,10))

"""py comanlineargu.py arg1, arg2, arg3"""

#Exercise 5

import random
random_number = random.randint(1, 10)
num = int(input('Guess the number between 1 to 10 in 3 tries'))
#print(random_number)
if num >= random_number:
    print('Guess lower')
if num < random_number:
    print('Guess higher')
try:
    for i in range(2):
        if num == random_number:
            print('The number ', num, ' you guessed is correct')
            break
        num = int(input('Try again'))
    else:
        raise Exception('Your retry exceeded. Please try again later')
except Exception as err:
    print(err)
    
#Exercise 6

try:
    inp = int(input('Enter the integer value'))
    a = 10 + '5'
    print(type(a))
    print('Value entered is ',inp)
except ValueError:
    print('Please enter the numeric value')
except TypeError:
    print('Please check the data type')
    
#Exercise 7

try:
    D1={'1':"aa", '2':"bb", '3':"cc"}
    print(D1['3'])
    l1 = [1,2,3]
    print(l1[3])
except KeyError:
    print('Key not present')
except IndexError:
    print('Index list out of range')

