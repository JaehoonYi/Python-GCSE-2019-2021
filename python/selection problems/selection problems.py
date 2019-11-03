#1
numOne = int(input("input a number: "))
if numOne < 100:
    print("the number you inputed is less than 100")
else:
    print("the number you inputed is more than 100")
    
#2
password = str(input("input a password:"))
if len(password) < 5 :
    print("your password is not long enough")
else:
    print("your password is long enough")

#3
passwordOne = str(input("enter your password: "))
passwordTwo = str(input("enter your password again: "))
if passwordOne == passwordTwo:
    print("your passwords match")
else:
    print("your passwords do not match")
                  
#4
year = int(input("enter a year:"))
numTwo = (year%4)
if numTwo  == 0: 
    print("the year you inputted is a leap year")
else:
    print("the year you iputted is not a leap year")
           
#5
numThree = int(input("enter a number:"))
if numThree//2 == 0:
    print("the number you entered is a even number")
else:
    print("the number you entered is odd number")
    
