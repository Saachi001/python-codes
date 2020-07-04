first = input("First String: ")
strn = input("String: ")
lenght = len(first)
ins_string = first[:int(lenght/2)] + strn + first[int(lenght/2):]
print(ins_string)