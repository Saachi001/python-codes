strn_1 = input("Enter String 1: ")
strn_2 = input("Enter String 2: ")
exc_1 = strn_2[-2:] + strn_1[2:-2] + strn_2[0:2]
exc_2 = strn_1[-2:] + strn_2[2:-2] + strn_1[0:2]
print("String 1: ", exc_1)
print("String 2: ", exc_2)