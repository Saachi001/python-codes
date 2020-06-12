#hwrite a program to swap three varaibles without using any extra variable to store value temporary 
# If the input variable are a, b, c, swap the value of a, b, & c and then c & a
# No extra variable should be used
a = int(input("Enter first Variable a: "))
b = int(input("Enter Second Variable b: "))
c = int(input("Enter Third Variable c: "))
a = a+b
b = a-b
a = a-b

print("a =", a)
print("b =", c)
print("c =", b)
