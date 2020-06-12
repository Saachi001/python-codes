#write a program to take the price of the 3 product for the resturant bill 
#and the tax percentage from the user and calculate final amount
#assume that the price of all the 3 product and the tax percentage will also be positive
#handle the decimal value for input and output
#tax amount = tax percentage/100*product price
a = float(input("Enter the price 1: "))
b = float(input("Enter the price 2: "))
c = float(input("Enter the price 3: "))
tax = float(input("Enter the tax %: "))
product_price = a + b + c 
tax_per = tax / 100
tax_amount = tax_per * product_price
total_amount = tax_amount + product_price
print("Final Amount: ", total_amount)