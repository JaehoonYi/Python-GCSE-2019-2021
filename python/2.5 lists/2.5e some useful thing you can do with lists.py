names = (["eee"]*5)
print(names)

names = ["rita", "sue"]
names.append("bob")
print(names) 

#there is actually a typo in the book. In the book, there is a square bracket after "bob" instead of a normal one

names = ["joe","nils","reece"]
extraNames = ["reece","nils","joe"]
names.extend(extraNames)
print(names) 

names = ["joe","nils","reece"]
extraNames = ["reece","nils","joe"]
names.append(extraNames)
print(names) 

names = ["joe","nils","reece"]
if ("reece") in names :
    print("reece is present")
if ("nils") in names :
    print("nils is present")
if ("joe") in names :
    print("joe is present")
if ("reece") in names :
    print("reece is present")

names = ["joe","nils","reece","Jae"]
if ("reece") in names :
    position = names.index("Jae")
    print("reece is in position",position)
else:
    print("404 reece not found")
    
names = ["joe","nils","Jae"]
if ("reece") in names :
    position = names.index("Jae")
    print("reece is in position",position)
else:
    print("404 reece not found")
    
