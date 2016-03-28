#!/usr/bin/python
#Map and Lambda
#The cubes of the first N Fibonacci numbers will be printed.

import math

def fibonacciCubes(n):
    #Find and print the cubes of the first N numbers in the fibonacci sequence
    fibList = []

    #Build a list of the first n fibonacci numbers.
    for y in range (0, n):
        fibList.append(fibonacciVal(y))

    #Define lambda function "cubes" to find the cube of each number.
    cubes = lambda x: int(math.pow(x, 3))

    #Print a list of the cubes.
    print (list(map(cubes, fibList)))        

def fibonacciVal(n):
    #Return the nth fibonacci number.
    if n == 2:
        return 1
    elif n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fibonacciVal(n-1) + fibonacciVal(n-2)

m = int(input())

fibonacciCubes(m)
