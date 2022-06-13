print("Enter three strings")

str1 = str(input("Enter the first string: "))
str2 = str(input("Enter the second string: "))
num = str(input("Enter a number: "))

print("Length of str1 is: ", len(str1))
print("Length of str2 is: ", len(str2))
print("Length of number entered is: ", len(num))

if(str1 == str2):
    print("str1 is equal to str2")
else:
    print("str1 is not equal to str2")
if(num == num[::-1]):
    print(num, " is a palindrome")
else:
    print(num, " is not a palindrome")

word = str(input("Enter a word: "))
sen = str(input("Enter a sentence strings: "))

if(sen.find(word)!= 1):
    print("Sentence entered contains \"", word, "\"")
    print("Hence", word, "is a substring")
else:
    print("Hence", word, "is not a substring")
