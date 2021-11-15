# Program 1: PUP Grading System
# Section 8 of https://www.pup.edu.ph/studentservices/files/ThePUPStudentHandbook2014.pdf
# Create a program that will ask for grade percentage. Display the equivalent Grade/Mark and Description
# Example:
# Input grade: 87.6
# Grade/Mark: 1.75
# Description: Very Good

import math

def gradingSystem():
    gradesF = float(input("Enter your grades: "))
    return gradesF

gradeF = gradingSystem()
grade = round(gradeF)

if grade >= 97:
    print("Grade/Mark: 1.00")
    print("Description: Excellent")
else:
    if grade > 93 and grade < 97:
        print("Grade/Mark: 1.25")
        print("Description: Excellent")
    else:
        if grade > 90 and grade < 94:
            print("Grade/Mark: 1.5")
            print("Description: Very Good")
        else:
            if grade > 87 and grade < 91:
                print("Grade/Mark: 1.75")
                print("Description: Very Good")
            else:
                if grade > 84 and grade < 88:
                    print("Grade/Mark: 2.00")
                    print("Description: Good")
                else:
                    if grade > 81 and grade < 85:
                        print("Grade/Mark: 2.25")
                        print("Description: Good")
                    else:
                        if grade > 78 and grade < 82:
                            print("Grade/Mark: 2.5")
                            print("Description: Satisfactory")
                        else:
                            if grade > 75 and grade < 79:
                                print("Grade/Mark: 2.75")
                                print("Description: Satisfactory")
                            else:
                                if grade == 75:
                                    print("Grade/Mark: 3.0")
                                    print("Description: Passing")
                                else:
                                    if grade > 64 and grade < 75:
                                        print("Grade/Mark: 5.0")
                                        print("Description: Failed")
                                    else:
                                        print("Grade/Mark:Inc/W/D")
                                        print("Descripton: Incomplete/Withdrawn/Dropped")
