# -*- coding: utf-8 -*-
""" Attia:  Exercises_24-06-2024.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TPPZMSWcxSslv696okPyrl75bvBWfKj5
"""



"""#Today Afternon with Eng. Ola  am 24.06.2024
Python Task 2 : Operators and conditions

Exercise 1: Basic Conditions Problem: Write a program that asks the user to input their age and then prints whether they are a minor (under 18), an adult (18-64), or a senior (65 and older).
"""

age = int(input("input your age = "))

if age < 18 :          print ("he is a minor ")

elif age > 18 and age < 65:           print ("he is a adult")
else :
          print ("he is a senior ")

""" Exercise 2: Comparison Operators
 Problem: Write a program that takes two numbers as input from the user and prints which one
is greater or if they are equal.
"""

x = int(input("input x = "))
y = int(input("input y = "))
if x >= y:
  print (x)

""" Exercise 3: Logical Operators
 Problem: Write a program that checks if a number input by the user is positive, even, and
greater than 10.
"""

a1 = int(input("input your Number = "))
if a1 > 0 and a1 > 10 and a1 % 2 == 0:
  print (" the number is positve, even and > 10 : ",a1)
else:
  print ("the number is negative oder or or less than 10 -:", a1)

"""Exercise 4: Nested Conditions
 Problem: Write a program that asks for the user's score on a test and prints the grade: 'A'
(90-100), 'B' (80-89), 'C' (70-79), 'D' (60-69), or 'F' (below 60).
"""

score = int(input("input your score = "))
if score > 90:
  print (" your score is ", score," and your grade is A ")
elif score > 80 and score < 89 :
    print (" your score is ", score," and your grade is B ")
elif score > 70 and score < 79 :
      print (" your score is ", score," and your grade is C ")
elif score > 60 and score < 69 : print (" your score is ", score," and your grade is D ")
else:
  print (" your score is ", score," and your grade is F ")

""" ##Exercise 5: Arithmetic Operators
 Problem:
 Write a program that asks the user to input two numbers and then prints the sum,
difference, product, and quotient of those numbers.
"""

x1 = int(input("input number x1 = "))
x2 = int(input("input number x2 = "))

def mysum(x,y):
  result = x+y
  return result
def mydif(x,y):
  result = x-y
  return result
def mypro(x,y):
  result = x*y
  return result
def myquo(x,y):
  if y == 0:
    print (" no result x2 is 0")
    return
  else:
   result = x/y
  return result

print ("sum numbers is ", mysum(x1,x2))
print ("diff numbers is ", mydif(x1,x2))
print ("prod numbers is ", mypro(x1,x2))
print ("quo numbers is ", myquo(x1,x2))

""" Exercise 6: Using elif
 Problem: Write a program that asks for the day of the week (1-7, where 1 is Monday and 7 is
Sunday) and prints whether it is a weekday or the weekend.
"""

d1 = int(input("input the day number 1-7 = "))
if d1== 1:
  print ("it's a weekday Monday")
elif d1==2 : print (" it's a weekday Tu")
elif d1==3 : print (" it's a weekday We")
elif d1==4 : print (" it's a weekday Th")
elif d1==5 : print (" it's a weekend Fi")
elif d1==6 : print (" it's a weekend Sa")
elif d1==7 : print (" it's a weekend Su")
else:
  print ("no Day")

""" Exercise 7: Modulus Operator
 Problem: Write a program that takes a number as input and prints whether it is odd or even.
"""

n1 = int(input("input your Number = "))
if n1 % 2 == 0:
  print ("the number is even", n1)
else:
  print ("the number is odd", n1)

""" Exercise 8: Multiple Conditions
 Problem: Write a program that asks the user to input a year and determines whether it is a leap
year or not.
"""

year = int(input("input your Number = "))
if year % 4 == 0:
  print ("the year is a leap", year)
else:
  print ("the year is not leap", year)

"""Exercise 9: Combining Input and Conditions
 Problem: Write a program that asks the user to input a number and then prints whether the
number is positive, negative, or zero.
"""



number = int(input("input your Number = "))
if number > 0: print ("the number is positive",  number)
elif number < 0: print ("the number is negative",  number)
else:
  print ("the number is zero", number)



"""Exercise 10: Basic Calculator
 Problem: Write a program that takes two numbers and an operator (+, -, *, /) as input and
performs the corresponding operation.
"""

def mysum(x,y):
  result = x+y
  return result
def mydif(x,y):
  result = x-y
  return result
def mypro(x,y):
  result = x*y
  return result
def myquo(x,y):
  if y == 0:
    print (" no result x2 is 0")
    return
  else:
   result = x/y
  return result

def main():
    x1 = int(input("input number x1 = "))
    x2 = int(input("input number x2 = "))
    x3 = input("input a operation from (+, -, *, /)  = ")

    if x3 == "+": print ("sum numbers is ", mysum(x1,x2))
    elif x3 == "-": print ("diff numbers is ", mydif(x1,x2))
    elif x3 == "*": print ("prod numbers is ", mypro(x1,x2))
    elif x3 == "/": print ("quo numbers is ", myquo(x1,x2))
    
if __name__ == "__main__":
    main()
