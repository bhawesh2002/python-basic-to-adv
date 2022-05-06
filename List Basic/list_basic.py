# prompt the user to enter the number of terms in list
terms = int(input("Enter the number of terms in the number list: "))

numbers = []  # declare the lsit of numbers

for i in range(0, terms):  # use of for loop to fill the number list
    # prompting the user to enter a number
    print("Enter the", i + 1, "number: ", end="")
    num = int(input())  # get input number from the user
    # use of append() function to add number entered by user into number list
    numbers.append(num)

# use of max() function to get maximum number in the list
print("The Maximum number in the list is: ", max(numbers))
# use of min() function to get minimum number in the list
print("The Minimum number in the list is: ", min(numbers))

# use of sum() function to calculate the sum of numbers in the number list
Sum = sum(numbers)
# formula to calculate avg of numbers
# use of len() function to calculate number of terms in the number list
Avg = Sum/len(numbers)
print("The Sum of numbers in the list is: ", Sum)  # print the sum of numbers
# print the average of numbers
print("The Averge of numbers in the list is: ", Avg)
print("The reverse of the list is: ")  # print the reverse of the list
# use of slicing to print the reverse of the list
print("Use of slicing: ", numbers[::-1])
# use of reverse() function to print the reverse of the list
revNumbers = numbers.reverse()
print("Using  reverse() function", revNumbers)
