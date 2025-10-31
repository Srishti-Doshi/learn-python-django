#Destructor
# variable memory accessability-> storage class : auto, extern, goto, static

import time
class Test:
    def __init__(self):
        print("constructor execution...")
    def __del__(self):
        print("destructor execution...")

List = [Test(), Test(), Test()]
del List
time.sleep(5)
print("End of application")