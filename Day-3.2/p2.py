class Demo:
    def __init__(self, a=None, b=None, c=None): 
        print("Value of a is {}, value of b {}, value of c is {}".format(a,b,c))

o1 = Demo() #Default argument
o2 = Demo(2)
o3 = Demo(2, 3)
o3 = Demo(4, 2, 3)
o4 = Demo(b=2,c=4) #Keyword argument
