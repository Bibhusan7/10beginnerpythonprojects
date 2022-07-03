std_id = input("Enter student's id: ")
std_name = input("Enter student's name: ")
sub1 = input("Enter marks of subject1: ")
sub2 = input("Enter marks of subject2: ")
sub3 = input("Enter marks of subject3: ")

std_id = int(std_id)
sub1 = int(sub1)
sub2 = int(sub2)
sub3 = int(sub3)

def student(std_id, std_name):
    return "Student ID: {}".format(std_id)+"\n"+"Student Name: {}".format(std_name)

def marks(sub1, sub2, sub3):
    summed = sub1+sub2+sub3
    return summed

def check_result():
    if average >= 40:
        print("Passed")
    else:
        print("Failed")


std = student(std_id, std_name)
print(std)

total = marks(sub1, sub2, sub3)
print("Total:", total)

average = total/3
print("Average:",average)

check_result()