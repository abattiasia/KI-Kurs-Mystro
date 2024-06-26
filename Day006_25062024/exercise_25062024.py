# -*- coding: utf-8 -*-
"""Exercise_25062024.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KN1wyvwTQK4lU6rM9b1P0f_NwL6YIGsz

# Exercise from Eng. Ola  25.06.2024

Exercise 1: For Loop
 Problem: Write a program that prints the numbers from 1 to 10 using a for loop.
"""

#Ex 01
for x in range(1,11):
    print(x)

""" Exercise 2: While Loop
 Problem: Write a program that asks the user to enter a positive number. Keep asking the user
 for a number until they enter a positive one. Once they enter a positive number, print it.
"""

#Ex 02
while True :
  x=int(input("Enter a positive number: "))
  if x>0 :
    print(x)
    break
  else:
    continue

"""Exercise 3: Nested Loops
 Problem: Write a program that prints a multiplication table for numbers 1 to 5. Use nested loops
 to generate the table.
"""

#Ex 03
for x in range(1, 6):
    for y in range(1, 6):
        print(x * y, end=" ")
        #print(f"{x} x {y} = {x * y}")

    print()

"""Exercise 4: Simple Function
 Problem: Write a function greet that takes a name as input and prints a greeting message,
 e.g., "Hello, [name]!".
"""

#Ex 04

def greet(name):

  print("Hello, {}!".format(name))

greet("Eng. Ola")

""" Exercise 5: Function with Loop
 Problem: Write a function countdown that takes a number as input and prints a countdown
 from that number to zero using a loop
"""

#Ex 05

def countdown(n):
  for i in range(n, -1, -1):
    print(i)

countdown(7)

"""Exercise 6: Function with Loop and Data Types (Lists)
 Problem: Write a function print_list that takes a list of strings as input and prints each
 string on a new line using a loop. Then, demonstrate the function with a list of your choice.
"""

#Ex 06
def print_list(kurs):
  for x in kurs:
    print(x)

my_list = ["python", "is", "a", "part", "of", "KI-Kurs"]
print_list(my_list)

"""Exercise 7: Using break and continue
 Problem: Write a program that asks the user to enter numbers. If the user enters a negative
 number, the program should stop asking for input (using break). If the user enters a number
 greater than 100, the program should ignore it (using continue). Print each valid number
 entered by the user
"""

# Ex 07
while True:
  user_input = int(input("Enter a number: "))  # input user data

  if user_input < 0:       # Check if the input is negative
    break

  elif user_input > 100:    # Check if the input is greater than 100
    continue

  else:
    print(user_input)    #  input is valid, print it



"""Exercise 8: Strings as Lists
 Problem: Write a function reverse_string that takes a string as input and returns the string
 reversed by treating it as a list of characters. Do not use any built-in string reversing methods
"""
def reverse_string(string):

  reversed_s= " "

  for char in string:
    reversed_s = char + reversed_s
  return reversed_s

def main():
    rr= reverse_string (" i have to write a program in python")
    print (rr)

if __name__ == "__main__":
    main()



