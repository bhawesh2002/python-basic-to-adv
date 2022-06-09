# enter the number of terms in array
terms = int(input("Enter the number of terms: "))
num = []  # array of numbers
print("Fill the array")  # print the message

for i in range(0, terms):  # loop to enter the numbers in array
    print("Enter the ", i + 1, " number")  # print the message
    element = int(input())  # enter the number
    num.append(element)  # append the number in array

even = []  # array of even numbers
odd = []  # array of odd numbers

for i in range(0, terms):  # loop to check even and odd numbers
    if(num[i] % 2 == 0):
        even.append(num[i])  # append even numbers in array
    else:
        odd.append(num[i])  # append odd numbers in array

print("Even numbers: ", even)  # print even numbers
print("Odd numbers: ", odd)  # print odd numbers
