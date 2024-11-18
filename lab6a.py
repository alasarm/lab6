#!/usr/bin/env python3
# Author ID: [seneca_id]

class Student:
    # Initialize attributes: name, number, and courses
    def __init__(self, name, number):
        self.name = str(name)  # Ensure name is a string
        self.number = str(number)  # Ensure number is always a string
        self.courses = {}

    # Return student name and number as a formatted string
    def displayStudent(self):
        return f'Student Name: {self.name}\nStudent Number: {self.number}'

    # Add a course and grade to the student's record
    def addGrade(self, course, grade):
        self.courses[course] = grade

    # Calculate and return GPA, handling division by zero
    def displayGPA(self):
        if len(self.courses) == 0:
            return f'GPA of student {self.name} is 0.0'
        gpa = sum(self.courses.values()) / len(self.courses)
        return f'GPA of student {self.name} is {gpa:.1f}'

    # Return a list of courses with passing grades (> 0.0)
    def displayCourses(self):
        return [course for course, grade in self.courses.items() if grade > 0.0]


# Test the class functionality if this script is run directly
if __name__ == '__main__':
    # Create first student object and add grades
    student1 = Student('John', 13454900)
    student1.addGrade('uli101', 1.0)
    student1.addGrade('ops245', 2.0)
    student1.addGrade('ops445', 3.0)

    # Create second student object and add grades
    student2 = Student('Jessica', 123456)
    student2.addGrade('ipc144', 4.0)
    student2.addGrade('cpp244', 3.5)
    student2.addGrade('cpp344', 0.0)

    # Display details for student1
    print(student1.displayStudent())
    print(student1.displayGPA())
    print(student1.displayCourses())

    # Display details for student2
    print(student2.displayStudent())
    print(student2.displayGPA())
    print(student2.displayCourses())

