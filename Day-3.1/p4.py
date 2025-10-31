# inner class is a member function of outer class, inner class can only be accessed with the help of object of outer class

class Outer:
    def __init__(self):
        print("Outer class object creation")

    class Inner:
        def __init__(self):
            print("inner class object creation")
        def m1(self):
            print("inner class method")

        class SubInner:
            def __init__(self):
                print("SubInner class object creation")
            def m2(self):
                print("SubIinner class method")

o = Outer()
i = o.Inner()
i.m1()

s = i.SubInner()
s.m2()