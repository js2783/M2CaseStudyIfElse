
'''
Author: Jody Smith
Date: 09/04/2025
Filename: M2 Case Study If Else While
Summary:Determine if a student qualifies for honor roll or dean's list
'''

def main():
    while True:
        studentLastName = input("Enter your last name: ") #gather user input
        if studentLastName == "zzz":
            print("End of Program")
            break
   
        #If program continues, define additional variables
        studentFirstName = input("Enter your first name: ")
        gpa = float(input("Enter your GPA: ")) #ensure number accepts decimals
        #evaluate input
        if gpa >= 3.5:
            print(f"{studentFirstName} {studentLastName}, you've made the the Dean's list!")
        elif gpa >= 3.25:
            print(f"{studentFirstName} {studentLastName}, you've made the honor roll.")
        else:
            print(f"{studentFirstName} {studentLastName}, you don't qualify for either Dean's list or Honor Roll at this time. Keep trying!")

main()