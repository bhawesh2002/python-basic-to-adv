# python program to calculate result of a student

print("======GRADE CALCULATOR======")
name = input("Enter Your Name: ")
print("Enter Your Marks in each subject")
subject_marks = ["English", "Marathi", "Maths", "Science", "Social Studies"]
for i in range(0, len(subject_marks)):
    print(subject_marks[i], ": ", end="")
    marks = float(input())
    subject_marks[i] = marks
print("============================")
total_marks = sum(subject_marks)
percentage = total_marks * (100/(len(subject_marks)*100))
print("TOTAL MARKS: ", total_marks)
print("PERCENTAGE: ", percentage, "%")
print("============================")
if(percentage > 85):
    print(name, " YOU ARE PASSED WITH DISTINCTION")
elif(percentage > 75):
    print(name, " YOU ARE PASSED WITH GRADE A")
elif(percentage > 60):
    print(name, " YOU ARE PASSED WITH GRADE B")
elif(percentage > 50):
    print(name, " YOU ARE PASSED WITH GRADE C")
elif(percentage > 45):
    print(name, " YOU ARE PASSED WITH GRADE D")
else:
    print("YOU ARE FAILED")
print("============================")
