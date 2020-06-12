#at few places, height are considered in feet and iches and weight in kg
#we need to solve this problem and get the height in cm and weight in pounds
# take the feety and inch part of the height and weight in the kg.
# Handle the decimal values also.
#You can assume that input is always positive.
# HInt: one foot is 12 inch and 1 inch is 2.54 cm, one kg is 2.3pounds
feet = float(input("Enter the height feet part: "))
inch = float(input("Enter the height inch part: "))
kg = float(input("Enter the weight in kg: "))
sub_inch = feet *12
total_inch = inch + sub_inch
cm = total_inch * 2.54
pound = kg * 2.2
print("Height in cm: ", cm)
print("Weight in pounds: ", pound)
