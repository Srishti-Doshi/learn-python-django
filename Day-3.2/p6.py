#Write a program to check whether entered Registration Number is valid or not (MP State)

import re
s = input("Enter Vehicle Registration Number: ")
m = re.match("MP[012][0-9][A-Z]{2}\d{4}", s)

if m != None:
    print("Valid Vehicle Registration Number")
else:
    print("InValid Vehicle Registration Number")
  