import sys
import os

def read(file_name):
    try:
        with open(file_name, "r") as student_details:
            print("Student Details")
            print("\t")
            for details in student_details:
                print(details.strip())
    except:
        print("File not present")

def update(parameter, update_para, file_name):
    try:
        with open(file_name, "r") as student_details:
            k = student_details.readlines()
        with open(file_name, "w") as student_details:
            for i in k:
                q = i.strip().split()
                if q[0] == update_para:
                    q[2] = str(parameter) + "\n"
                    w = " ".join(q)
                    student_details.write(w)
                else:
                    student_details.write(i)
    except:
        print("File not present")

def add(roll_no, name, age, language):
    file_name = "database/{}.txt".format(roll_no)
    with open(file_name, "w") as student_details:
        details = "Rollno : {}\nName: {}\nAge : {}\nLanguage : {}\n".format(roll_no, name, age, language)
        student_details.write(details)

if len(sys.argv) != 3:
    print("It is not correct")
    sys.exit()

student_roll_number = sys.argv[1]
task = sys.argv[2]
file_name = "database/{}.txt".format(student_roll_number)

if task == "read":
    read(file_name)
elif task == "update":
    print("1.Name\n2.Age\n3.Language")
    update_para = int(input("Enter the option need to update:"))
    if update_para == 1:
        name = input("Enter the Name:")
        while not all(c.isalpha() or c in [' ', '.'] for c in name):
            print("Invalid input. Name should not contain numbers or special characters (except space and period).")
            name = input("Enter the Name:")
        update(name, "Name", file_name)
    elif update_para == 2:
        age = int(input("Enter the Age:"))
        while not (age >= 5 and age <= 16):
            age = int(input("Enter the Age:"))
        update(age, "Age", file_name)
    elif update_para == 3:
        language = input("Enter the Language:")
        while not language.isalpha():
            language = input("Enter the Language:")
        update(language, "Language", file_name)
    else:
        print("Enter a valid option")
elif task == "add":
    roll_no = sys.argv[1]
    name = input("Enter the Name:")
    age = int(input("Enter the Age:"))
    language = input("Enter the Language:")
    add(roll_no, name, age, language)
elif task == "delete":
    os.remove("database/{}.txt".format(sys.argv[1]))
else:
    print("Invalid task specified")
