'''
Exception Handling

try:
Risky Code

except:
will be executed if there is exception inside try

else:
will be executed if there is no exception inside try

finally:
will be executed whether exception raised or not raised and handled or not handled

'''

# a, b, c = 40, 5, 0
# for i in range(1,10):
#     c = a//b
#     print(c)
#     b = b-1

# print("Hello")

a, b, c = 40, 5, 0
try:
    for i in range(1,10):
        c = a//b
        print(c)
        b = b-1
    print("This will never run")
    print("after exception occurs in try the control will be given to except")
except ZeroDivisionError:
    print("Except working")

print("Hello")