# id name post location

class Employe:
    def __init__(self, id , name, post, location):
        self.id = id
        self.name = name
        self.post = post
        self.location = location
        
    def show(self):
        print("Employe ID: ",self.id)
        print("Employe name: ",self.name)
        print("Employe post: ",self.post)
        print("Employe location: ",self.location)

    def deletelocation(self):
        del self.location      # delete instance variable within class

d1 = Employe(123, "Sonu", "Director", "Dewas")
d1.show()

#del d1.post      # delete instance variable outside class
#d1.deletelocation()
d1.show()