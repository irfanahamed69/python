##Given a list ['a', 'b', ...] print elements along with their position like 0: a, 1: b one per line
Lis = ['a','b']
for i in Lis:
  print (str(Lis.index(i)) + ': ',i)
  
##Loop over a dict and print the value and key in the format value belongs to key
dict = {'a': 1, 'b': 2}
for key, value in dict.items():
    print('Value ' + str(value) + ' belongs to key ' + key)
	
##write an add function that accepts two numbers and returns their sum
def add(num1: int, num2: int):
    """we are using typehints"""
    return num1 + num2
    
print(add(5, 5))

##write a function that accepts any number of args and prints them to the screen one per line
def argument(*args):
    for i in args:
        print(i)

argument('jack', 'jill')

##write a function that accepts any number of kwargs and prints the number of orgs
def argument(**args):
    print('The total number of argument received is ' + str(len(args)))

argument(name="Jack", country="IN")

##write a function that accepts any number of args and/or kwargs and prints the count of both
def argument(*args, **keys):
    print('The total number of argument received is ' + str(len(args)))
    print('The total number of Keyword argument received is ' + str(len(keys)))

argument('name', 'country', name="Jack", country="IN")

##Do list comprehension to get odd numbers' squares from this list: [1, 3, 3, 4, 5, 6]
lis = [1, 3, 3, 4, 5, 6]
newlis = [pow(int(x), 2) for x in lis if x % 2 != 0]

print(newlis)

##write a lambda expression to return average given a total and count
avg = lambda a,b: (a + b)/2
print(avg(5,10))

##while loop without else block getting invoked
num = 1
while num < 10:
    if (num % 2 == 0):
        print(num)
        break
    num = num + 1
else:
    print('Loop Completed after', num, ' iterations')
    
##while loop with else block getting invoked
num = 1
while num < 10:
    if (num % 2 == 0):
        print(num)
    num = num + 1
else:
    print('Loop Completed after', num, ' iterations')
    
##Try list comp to get keys that are longer than 4 chars in a dict
dict = {'colour':'blue','name':'ozil','company':'abc'}
listcomp = [x for x in dict.keys() if len(x) > 4]
print(listcomp)

##implement nested list comp in any use case
dict = {'colour':'blue','name':'ozil','company':'abc'}
listcomp = [y for y in [x for x in dict.keys() if len(x) > 4] if y == 'colour']
print(listcomp)

##Improvise the guessing game from yesterday by providing 3 tries to the player
import random
random_number = random.randint(1, 10)
num = int(input('Guess the number between 1 to 10 in 3 tries'))
#print(random_number)
if num >= random_number:
    print('Guess lower')
if num < random_number:
    print('Guess higher')
for i in range(2):
    if num == random_number:
        print('The number ', num, ' you guessed is correct')
        break
    num = int(input('Try again'))
else:
    print('Sorry retries exceeded')
