class Test:
    def __init__(self, *a):  #variable length argument
        sm = 0
        for i in a:
            sm = sm + i
        print("Sum = ",sm)

t1 = Test()
t2 = Test(10)
t3 = Test(10, 20)
t4 = Test(10, 20, 30)
t5 = Test(100, 200, 300, 400)

''' In *a , what is type of a?
a is a tuple.
Explanation:
The * (asterisk) before a parameter name means “collect all remaining positional arguments into a tuple".'''