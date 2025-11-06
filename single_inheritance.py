# single inheritance

class animal:
    def sound(self):
        print("Animal sound")
class dog(animal):
    def bark(self):
        print("Bark")

d=dog()
d.sound()
d.bark()
