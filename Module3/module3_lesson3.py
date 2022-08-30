#Creating a parent class called Students
class Students:
#defining a method of the class
    def __init__(self, first_name, last_name, student = []):
        self.first_name = first_name
        self.last_name = last_name
        self.email = first_name + '.' + last_name + '@stutern.com'
    # print("check")  

#Creating objects of the parent class
stud_1 = Students("Bukola", "Dare")
stud_2 = Students("Temitope", "Balogun") 
# print(stud_2.last_name)

#Creating a sub-class called Group_leader
class Group_leader(Students):
#defining a method of the sub-class
    def __init__(self, first_name, last_name, student=[]):
        super().__init__(first_name, last_name)
        self.student = student 
           
    # print("sub-class created") 

#Defining a method that adds to the list of students under the group leader
    def add_students(self, student):
        self.student.append(student)
        print(self.student, student)
    # print("add method created")

#Defining a method that removes students from the list of students under the group leader
    def remove(self, student):
        self.student.remove(student)
        print(self.student, student)
    
    # print("item removed successfully")

#Defining a method that prints out the full names of students in the list of students under group leader
    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)

#adding three more objects of the parent class.
stud_3 = Students("Haleemah", "Mama") 
stud_4 = Students("Abdulganiyu", "Bobo") 
stud_2 = Students("Abdulkareem", "Ramadan")
#print(stud_3.first_name)

#Creating 2 instances of the sub class you.
Groupleader_1 = Group_leader("Great", "Water")
Groupleader_2 = Group_leader("Robbin", "Sand")
# print(Groupleader_1.first_name)

#Adding 2 students to the list of students under the objects of my subclass.
# Groupleader_1.add_students("olamide")
# Groupleader_1.add_students("fola")
# Groupleader_2.add_students("martha")
# Groupleader_2.add_students("Tania")

#Remove 1 student each from the list of students under the objects of your subclass
# Groupleader_1.remove("olamide")
# Groupleader_2.remove("martha")

#Print the full name of the students in the list of students under the objects of your subclass.
print(Groupleader_1.fullname())
print(Groupleader_2.fullname())

#Print the email of the objects of your subclass.
def email(self, first_name, last_name):
    self.email = first_name + '.' + last_name + '@stutern.com'
print(Groupleader_1.email)
print(Groupleader_2.email)