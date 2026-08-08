total = 0

#Reads 4 prices from the user (using a for loop)
for i in range(4):
    price = float(input("Enter the price"))
    total += price
#Calculates the sum of the prices
average = total / 4

#Displays the sum and average, each with 2 decimal places
print("Total =", format(total, ".2f"))
print("Average = ", format(average, ".2f"))