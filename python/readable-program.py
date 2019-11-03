#the code is very readable

input1=int(input("enter a number: "))
input2=int(input("enter a number: "))
input3=int(input("enter a number: "))

inputTotal=int(input1+input2+input3) 
inputAverage = inputTotal/3
biggestInput = input1


#this program will see which input is the largest

if input1>input2 and input1>input3:
    biggestInput = str(input1)

elif input2>input1 and input2>input3:
    biggestInput = str(input2)

else:
    biggestInput = str(input3)

print("the total of the 3 inputed numbers is",inputTotal,", the average of the inputed numbers is",inputAverage,"and the biggest input is",biggestInput)



