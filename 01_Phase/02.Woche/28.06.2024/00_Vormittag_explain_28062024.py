dir()
import requests

x = requests.get('https://w3schools.com/python/demopage.htm')

print(x.text)


from os import chdir, mkdir  # gut falls man weiss genau
import os
from os import *
