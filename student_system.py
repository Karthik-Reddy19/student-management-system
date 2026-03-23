#Student Management System using file handling

#Class to represent a student
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    #Display student details
    def display(self):
        print("Name of the Student:",self.name)
        print("Marks obtained:",self.marks)
        if self.marks>=35:
            print("Pass")
        else:
            print("Fail")
#Function to add new student
def add():
    name=input("Enter the name of the student:")
    marks=int(input("Enter the marks of the student:"))
    with open("student.txt","a") as f:
        f.write(name+","+str(marks)+"\n")
#Function to display all student records
def display_all():
    try:
        with open("student.txt", "r") as f:
            data = f.readlines()
            #Check if the file is empty or not
            if not data:
                print("No records found")
                return
            #Access each record and display
            for line in data:
                name, marks = line.strip().split(",")
                s = Student(name, int(marks))
                print("\n--- Student ---")
                s.display()

    except FileNotFoundError:
        print("File not found")
# Function to search for a student using name
def search():
        search_name=input("Enter the name of the student:")
        found=False
        with open("student.txt", "r") as f:
           for line in f:
            name, marks = line.strip().split(",")
            if name.lower() == search_name.lower():
                s = Student(name, int(marks))
                print("\nRecord Found:")
                s.display()
                found = True
                break
        if not found:
                 print("NO record found")
#Function to delete student using name
def delete_student():
    de=input("Enter the name to be removed:")
    found=False
    new_data = []

    with open("student.txt", "r") as f:
        for line in f:
            name, marks = line.strip().split(",")
            if name.lower() != de.lower():
                new_data.append(line)
            else:
                found = True

    with open("student.txt", "w") as f:
        f.writelines(new_data)

    if found:
        print("Record deleted")
    else:
        print("No record found")
#Function to update students marks

def update_student():
    uname=input("Enter the name of the student:")
    found=False
    new_data = []

    with open("student.txt", "r") as f:
        for line in f:
            name, marks = line.strip().split(",")
            if uname.lower() == name.lower():
                new_marks = input("Enter new marks: ")
                new_data.append(name + "," + new_marks + "\n")
                found = True
            else:
                new_data.append(line)

    with open("student.txt", "w") as f:
        f.writelines(new_data)

    if found:
        print("Record updated")
    else:
        print("No record found")

    if not found:
         print("no records")
         
#Main Menu
def menu():
    while True:
            print("\n1.Add Student\n2.Search \n3.Display all\n4.Delete\n5.Update\n6.Exit")
            try:
                choice=int(input("Enter the choice:"))
            except ValueError:
                print("Please enter a valid choice")
            if choice==1:
                add()
            elif choice==2:
                search()
            elif choice==3:
                display_all()
            elif choice==4:
                delete_student()
            elif choice==5:
                update_student()
            elif choice==6:
                break
            else:
                print("Invalid choice.Try again")

if __name__=="__main__":
    menu()


