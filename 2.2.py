class animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print(self.name,"makes a sound")

class dog(animal):
    def speak(self):
        print(self.name,"barks")

class cat(animal):
    def speak(self):
        print(self.name,"mewows")

ani=input("Enter dog/cat:")
name=input("Enter name:")
if ani=="dog":
    pet=dog(name)
else:
    pet=cat(name)

pet.speak()

      
