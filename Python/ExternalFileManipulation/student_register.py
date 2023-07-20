# entering the number of students that will be registered
number_of_students = input("How many students will be registering? : ")

# creating a file "reg_form.txt" to write in
file = open("../../../AMS-TRAINING/Python/ExternalFileManipulation/reg_form.txt", "w")

# for loop for the amount of students that will be registered, later the data is saved in the file
for student in range(1, int(number_of_students)+1):
    ID = input(f"Please enter your student ID - Student {student} : ")
    file.write(f"\n Student {student} ID number is : {ID}")
