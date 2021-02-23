#Exercise 1

def gen(inp):
    for x in range(len(inp)-1,-1,-1):
        yield inp[x]

x = gen('hello')
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print('\n')

y = gen('python')
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))

#Exercise 2

class dunder():
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __add__(self,c):
        return (self.a + c - self.b)

x = dunder(7,3)
print(x.__add__(2)) 

x = dunder(6,3)
print(x.__add__(2)) 

#Exercise 3

import timeit

def dec(func):
    def wrapper(num):
        start_time = timeit.default_timer()
        print('start time ',start_time)
        print(func(num))
        End_Time = timeit.default_timer()
        print('End time ',End_Time)
        print('Time taken is ',End_Time - start_time)
    return wrapper

@dec
def fact(num):
    fact = 1
    for x in range(1,num+1):
       fact = fact * x
    return fact

fact(3)



