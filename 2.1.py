class car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def start(self):
        print(self.model,"car is starting")
    def stop(self):
        print(self.model,"car is stopping")

make=input("Enter car make")
model=input("Enter car make")
year=input("Enter car make")

mycar=car(make,model,year)
mycar.start()
mycar.stop()


