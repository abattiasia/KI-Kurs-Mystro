# -*- coding: utf-8 -*-
"""00_Morning_Explain_27062024.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TxMtwbpDxWSjTSf3VY6uCDFa28P9LKmz
"""



"""'''
Explain am 27.06.2024

- review ->
- class
- object
-


'''
"""

class Calc:
  def __init__(self,name):
    print (f"welcom {name}")
  def sum(self,x,y):
    return x+y

  def mul(self,x,y):
    return x*y

s= Calc("abdou")
print(s.sum(5,5))
print(s)

class A:
  def do(self):
    print ("in A")