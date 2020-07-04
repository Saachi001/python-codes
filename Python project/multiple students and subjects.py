mark_all = input()
marks_student = mark_all.split(";")
marks_student1 = marks_student[0].split(",")
marks_student2 = marks_student[1].split(",")
marks_student3 = marks_student[2].split(",")
marks_student4 = marks_student[3].split(",")
avg_subject1 = (int(marks_student1[0]) + int(marks_student2[0]) + int(marks_student3[0]) + int(marks_student4[0]))/4
avg_subject2 = (int(marks_student1[1]) + int(marks_student2[1]) + int(marks_student3[1]) + int(marks_student4[1]))/4
avg_subject3 = (int(marks_student1[2]) + int(marks_student2[2]) + int(marks_student3[2]) + int(marks_student4[2]))/4
avg_subject4 = (int(marks_student1[3]) + int(marks_student2[3]) + int(marks_student3[3]) + int(marks_student4[3]))/4
avg_subject5 = (int(marks_student1[4]) + int(marks_student2[4]) + int(marks_student3[4]) + int(marks_student4[4]))/4
print("subject Average: ",avg_subject1)
print("subject Average: ",avg_subject2)
print("subject Average: ",avg_subject3)
print("subject Average: ",avg_subject4)
print("subject Average: ",avg_subject5)