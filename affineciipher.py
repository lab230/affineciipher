Python 3.3.3 (v3.3.3:c3896275c0f6, Nov 18 2013, 21:19:30) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #Prints a transposition table for an affine cipher.
#a must be coprime to m=26.
def affine(a, b):
    for i in range(26):
        print chr(i+65) + ": " + chr(((a*i+b)%26)+65)
 
#An example call
affine(9, 11)
SyntaxError: invalid syntax
>>> #Prints a transposition table for an affine cipher.
#a must be coprime to m=26.
def affine(a, b):
    for i in range(26):
        print char(i+65) + ": " + char(((a*i+b)%26)+65)
 
#An example call
affine(5, 8)

SyntaxError: invalid syntax
>>> SyntaxError: invalid syntax
SyntaxError: invalid syntax
>>> import stdio.h
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    import stdio.h
ImportError: No module named 'stdio'
>>> 
>>> ================================ RESTART ================================
>>> 
>>> import random as rd
import math as m
def permutationByRecursion(input, s, li):
    if len(s) == len(input):
        li.append(s)
    for i in range(len(input)):
        if input[i] not in s:
            s+=input[i]
            permutationByRecursion(input, s, li)
            s=s[0:-1]
            
SyntaxError: multiple statements found while compiling a single statement
>>> 
import random as rd
import math as m
def permutationByRecursion(input, s, li):
    if len(s) == len(input):
        li.append(s)
    for i in range(len(input)):
        if input[i] not in s:
            s+=input[i]
            permutationByRecursion(input, s, li)
            s=s[0:-1]
            
SyntaxError: multiple statements found while compiling a single statement
>>> res=[]
#permutationByRecursion('abcdefghijklmnopqrstuvwxyz', '', res)
>>> 
import math as m
def permutationByRecursion(input, s, li):
    if len(s) == len(input):
        li.append(s)
    for i in range(len(input)):
        if input[i] not in s:
            s+=input[i]
            permutationByRecursion(input, s, li)
            s=s[0:-1]

import random as rd
import math as m
def permutationByRecursion(input, s, li):
    if len(s) == len(input):
        li.append(s)
    for i in range(len(input)):
        if input[i] not in s:
            s+=input[i]
            permutationByRecursion(input, s, li)
            s=s[0:-1]
            
SyntaxError: multiple statements found while compiling a single statement
>>> res=[]
#permutationByRecursion('abcdefghijklmnopqrstuvwxyz', '', res)

>>> res=[]
#permutationByRecursion('abcdefghijklmnopqrstuvwxyz', '', res)
[DEBUG ON]
>>> 
[DEBUG OFF]
>>> ================================ RESTART ================================
>>> import math as m
>>> def permutationByRecursion (input, s, li):
	if len(s) == len(input):
		li.append(s)
	for i in range (len(input)):
		if input[i] not in s:
			s++input [i]
			permutationByRecursion(input, s, li)
			s=s[0:-1]
res[]
SyntaxError: invalid syntax
>>> res=[]
>>> #permutationByRecursion ('abcdefghijklm...z', ", res)
>>> 
