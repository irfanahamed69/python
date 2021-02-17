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