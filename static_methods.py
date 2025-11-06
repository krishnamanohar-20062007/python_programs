# static methods

class aditya:
    @staticmethod
    def add(x,y):
        print("sum=",x+y)
    @staticmethod
    def sub(x,y):
        print("difference=",x-y)
    @staticmethod
    def avg(x,y):
        print("Average=",(x+y)/2)

aditya.add(200,100)
aditya.sub(200,100)
aditya.avg(200,100)
