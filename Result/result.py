# python program to print result of student

print("Result System")

name = input("Enter your name:")

print("Enter your subjectwise marks")

maths = float(input("Maths:"))
english = float(input("English:"))
science = float(input("Science:"))
marathi = float(input("Marathi:"))
social_studies = float(input("Social Studies:"))

sum = maths + english + science + marathi + social_studies

print("Total Marks = ", sum)

percentage = sum/500*100

print("Percentage = ", percentage , "%")

if(percentage >= 90):
    print("Conguratulations! You have secured A grade")
elif(percentage >= 80):
    print("Conguratulations! You have secured B grade")
elif(percentage >= 70):
    print("Conguratulations! You have secured C grade")
elif(percentage >= 60):
    print("Conguratulations! You have secured D grade")
else:
    print("Fail")
