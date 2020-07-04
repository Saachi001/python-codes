from math import*
calculator = True
last_result = 0
while calculator:
    a = input(">")
    if a in ('q', "Q"):
        calculator = False
    elif a in ('c', "C"):
        last_result = 0
    else:
        result = eval(a) + last_result
        last_result = result
        print(last_result)