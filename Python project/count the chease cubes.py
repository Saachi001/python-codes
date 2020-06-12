#there is a tray hjaving cheese cubes, we need tyo count the cheesese cubes in the tray,
#one cube can not be placed above another.
#We can ask user for the dimension of the box(lenght, width) can be asked from the user also the size of the side of cube
#for the box, lenght and width can be different. for the cheese cubes, lenght and width will be the same.
#Assumption, there will be no left out space/gap on the tray in between or in sides. all input /output will be numbers and no decimal value.
lenght_tray = int(input("Enter the tray's lenght: "))
width_tray = int(input("Enter the tray's width: "))
side_cube = int(input("Enter the side of cube: "))
first_side = lenght_tray / side_cube
second_side = width_tray / side_cube
total_side = first_side * second_side
print("Number of Cubes: ", total_side)