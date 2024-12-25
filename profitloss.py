i = float(input("Your buying price for oranges(in pounds): "))
x = float(input("Your selling price (in pounds): "))
if (x > i):
    print("Total profit is £{0}".format(x - i))
elif (x < i):
    print("Total loss is £{0}".format(i - x))
else:
    print("No profit in total.")