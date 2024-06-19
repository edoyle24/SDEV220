"""
Eric Doyle
M02 Lab - Case Study
The app will take a student's name and GPA and determine if they qualify for the Dean's List or Honor Roll
"""

#Take the user inputs for the students first name, last name, and GPA#
last_name = str(input("Please enter the student's last name: "))
first_name = str(input("Please enter the student's first name: "))
gpa = float(input("Please enter the student's GPA: "))

#test if the user entered a valid last name#
if last_name == 'ZZZ':
    print("Please enter a valid last name")
#test if the student has a high enough GPA to make the Dean's List#
elif(gpa >= 3.5):
    print("The student has made the Deans's List.")
#test if the student has a high enough GPA to make the honor roll
elif(gpa >= 3.25):
    print("The students has made the honor roll.")
#if the student does not have a GPA high enough for either let the user know the student did not make either list
else:
    print("The student has not made the Dean's List or Honor Roll.")