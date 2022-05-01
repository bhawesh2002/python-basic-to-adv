terms = int (input("Enter the number of terms in the number list: "))   #prompt the user to enter the number of terms in list

numbers = []    #declare the lsit of numbers

for i in range (0,terms):   #use of for loop to fill the number list
    print("Enter the", i + 1 ,"number: ", end = "") #prompting the user to enter a number
    num = int (input()) #get input number from the user
    numbers.append(num) #use of append() function to add number entered by user into number list

print ("The Maximum number in the list is: ", max(numbers)) #use of max() function to get maximum number in the list
print ("The Minimum number in the list is: ", min(numbers)) #use of min() function to get minimum number in the list

Sum = sum(numbers)  #use of sum() function to calculate the sum of numbers in the number list
#formula to calculate avg of numbers
Avg = Sum/len(numbers) #use of len() function to calculate number of terms in the number list 
print("The Sum of numbers in the list is: ", Sum)  #print the sum of numbers
print("The Averge of numbers in the list is: ", Avg) #print the average of numbers
