'''
Write a Python program to check whether gmail id is valid or not?
'''
import re
n = input("Enter Gmail ID: ")
m = re.match("\w[a-zA-Z0-9_.]*@gmail[.]com", n)

if m != None:
    print("valid")
else:
    print("Invalid")
