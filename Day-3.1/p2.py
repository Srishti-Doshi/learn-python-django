class Student:
    def __init__(self, sname, rollno, mob):
        self.sname = sname
        self.rollno = rollno
        self.mob = mob

    def show(self):
        print("StudentName= ",self.sname)
        print("RollNo= ",self.rollno)
        print("MOB= ",self.mob)

d1 = Student("Raj", 23233, 9987865)
d2 = Student("Jay", 8453, 8767865)
d3 = Student("Kunal", 7633, 9467785)

d1.show()
d2.show()
d3.show()
        