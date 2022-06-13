print("Enter three strings")  # Prompt the user to enter strings

str1 = str(input("Enter the first string: "))  # Enter the first string
str2 = str(input("Enter the second string: "))  # Enter the second string
num = str(input("Enter a number: "))  # Enter a number in the form of string

print("Length of str1 is: ", len(str1))  # print the length of the str1
print("Length of str2 is: ", len(str2))  # print the length of str2
print("Length of number entered is: ", len(num))  # print the length of num

if(str1 == str2):  # check if str1 is equal to str 2
    print("str1 is equal to str2")  # print the result
else:
    # print the result if str1 is not equal to str 2
    print("str1 is not equal to str2")
if(num == num[::-1]):  # reverse the string using slicing operator
    print(num, " is a palindrome")  # print the result
else:
    # print the result if num is not palindrome
    print(num, " is not a palindrome")
print("=====CHECK FOR SUBSTRING=====")
word = str(input("Enter a word: "))  # Enter a word
sen = str(input("Enter a sentence strings: "))  # Enter a sentence

if(sen.find(word) != 1):  # USe find function to find "word" in "sen"
    print("Sentence entered contains \"", word, "\"")  # print the result
    print("Hence", word, "is a substring")
else:
    print("Hence", word, "is not a substring")#print the result is "word" is not in "sen"
