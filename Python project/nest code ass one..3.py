#write a program to take one number say n as inputed from the user and print the sum of first n intergers
#user will enter single number
#assume user will always give positive number as input
#sum of the intergers can be computer using using formula: sum =n(n+1)/2
n = int(input("Enter the number: "))
sum = 0
for num in range(0, n+1, 1):
    sum = sum+num
print("The Sum is : ", sum)
