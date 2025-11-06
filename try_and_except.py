# try and except
'''while True:
    try:
        num=int(input("Enter the number"))
        print(num)
    except ValueError:
        print("The entered value is invalid . Please enter an integer")
        break

print("try and except are over")'''

'''try:
    print(10/0)
except ZeroDivisionError:
    print("cannot divide with zero")'''


while True:
    try:
        num=int(input("Enter the number"))
        print(10/num)
    except ValueError:
        print("The entered value is invalid . Please enter an integer")
        break
    except ZeroDivisionError:
        print("cannot divide with zero")
    else:
        print("No exceptions occured")
    finally:
        print("Execution completed")

print("try and except are over")
