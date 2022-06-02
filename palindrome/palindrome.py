# python program to check weather a number is palindrome or not

number = int(input("Enter A Number: "))
temp1 = number  #store number in temp1 variable
temp = int(0)  #temp variable
sum = int(0)   #sum var to store reverse
while(temp1 != 0):   #iterate the loop until temp1 is not equal to zero
    temp = int(temp1 % 10)  #store the last digit in temp
    sum = (sum * 10) + temp #multiply sum by 10 then add temp to it to generate reverse
    temp1 = int(temp1 /10)  #divide temp1 by 10 to eleminate last digit
print (int(sum))  #print reverse obtained

if(number == sum):  #check is number entered is palindrome or not
    print (number , " is a palindome")
else:
    print(number , " is not a palindome")
