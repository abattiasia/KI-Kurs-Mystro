# -*- coding: utf-8 -*-
"""Exercise_27062024.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13myebTRf3CBR4U_3n2SLlxfycbTK9i0s

# Exercise at 27.06.2024 from Eng. Ola

- Project Zoo Mamnagment System
- Exercise for Classes and Functions

#Exercise: Zoo Management System

Objective:

Create a simple Zoo Management System using inheritance. You will create a base class
Animal and derive specific animal classes from it.

Instructions:

1. Create a base class Animal:
This class should have the folowing attributes:
name: the name of the animal (string)
age: the age of the animal (integer)
species: the species of the animal (string)
This class should have the following methods:
    --init_-(self, name, age, species): constructor to initialize the
attributes.
make_sound (self):a method that prints a general sound, like "Some
generic animal sound".
2. Greate subclasses for specific animals:
Create at least three subclasses that inherit from Animal. For example, Lion,
Elephant, and Monkey.
Each subclass should overide the make_sound method to print a sound specific
to that animal. For example, a lion might roar, an elephant might trumpet, and a
monkey might chatter.
Add an additional attribute or method to each subclass that is specific to that
animal. For example, Lion could have an attribute mane_size and a method
hunt, Elephant could have an attribute trunk_length and a method
swing_trunk, and Monkey could have an attribute tail_length and a
method swing.
3. Test the classes:
Create instances of each subclass and test their methods.
Print out the details of each animal (name, age, species) and call their
make_sound method.
"""

"""
1. Create a base class Animal:
This class should have the folowing attributes:
--> name: the name of the animal (string)
-->age: the age of the animal (integer)
--> species: the species of the animal (string)
This class should have the following methods:
-->   --init_-(self, name, age, species): constructor to initialize the attributes.
--> make_sound (self):a method that prints a general sound, like
-->  "Some  generic animal sound".
"""
class Animal:
  def __init__(self, name, age, species):
    self.name = name
    self.age= age
    self.species = species

  def make_sound(self):
    print("Some generic animal sound")

"""
2. Greate subclasses for specific animals:
Create at least three subclasses that inherit from Animal.
For example, Lion, Elephant, and Monkey.

Each subclass should overide the make_sound method to print a sound specific
to that animal.

For example,
--> a lion might roar,
--> an elephant might trumpet,
--> and a monkey might chatter.

Add an additional attribute or method to each subclass that is specific to that
animal. For example,
--> Lion could have an attribute mane_size and a method hunt,
--> Elephant could have an attribute trunk_length and a method swing_trunk, and
--> Monkey could have an attribute tail_length and a method swing.

"""

# 01
class Lion(Animal):
  def __init__(self, name, age, species, mane_size ):
    super().__init__(name, age, species)
    self.mane_size= mane_size

  def make_sound(self):
    print(f"{self.name} roar")

  def hunt(self):
    print(f"{self.name} hunts")

#02
class Elephant(Animal):
  def __init__(self, name, age, species, trunk_length):
    super().__init__(name, age, species)
    self.trunk_length= trunk_length

  def make_sound(self):
    print(f"{self.name} trumpet")

  def swing_trunk(self):
    print(f"{self.name}  trunks")

#03
class Monkey(Animal):
  def __init__(self, name, age, species, tail_length ):
    super().__init__(name, age, species)
    self.tail_length= tail_length

  def make_sound(self):
    print(f"{self.name}  chatter")

  def swing(self):
    print(f"{self.name}  swings")

l= Lion("Lion01", 10, "  Lion", "small")
e= Elephant("Elephant01", 50, " elephant", "big")
m= Monkey("Monkey01", 5, " Monkey", " long")


l.hunt()
l.make_sound()

e.swing_trunk()
e.make_sound()

m.make_sound()
m.swing()