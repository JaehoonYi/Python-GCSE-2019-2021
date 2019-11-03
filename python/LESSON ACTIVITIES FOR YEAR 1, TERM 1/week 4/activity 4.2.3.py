bill = int(input("how much was the meal?: "))
tip = int(input("what % would you like to tip: "))
print ("you tipped {0:.0f}%".format(tip))
billPercentage = int(bill/100)
tipTotal = int(billPercentage*tip)
billTotal = int(tipTotal+bill) 
print("your total is",billTotal,".")
print("you tipped",tipTotal,".")



