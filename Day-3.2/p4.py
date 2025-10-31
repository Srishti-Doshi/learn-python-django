'''
Regular expression to represent all 10 digit mobile numbers.
Rules:-
1)Every number should contain atleast 10 numbers.
2)first digit should be 7 or 8 or 9
'''
import re
n = input("Enter mobile number: ")
m = re.match("[7-9][0-9]{9}", n)
# m = re.match("[7-9]\d{9}", n)
# m = re.match("[7-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]", n)

if m != None:
    print("valid")
else:
    print("Invalid")
