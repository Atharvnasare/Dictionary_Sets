Write a Program to enter a marks of 3 subject from the uses and store them in a dictionary starts with an empty dictionary and add one by one 

marks = {}

x = int(input("Enter a Phy :"))
marks.update({"Phy" : x})

x = int(input("Enter a Math :"))
marks.update({"Math" : x})

x = int(input("Enter a Bio :"))
marks.update({"Bio" : x})

print(marks)
