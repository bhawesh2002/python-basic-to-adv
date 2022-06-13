print("****Calculate Your FInal Salary****")       #Display the text 
basic = float(input("Enter your basic salary: "))  #Prompting user to  enter salary

hra = basic * 10/100        #Calculate HRA
ta = basic * 5/100          #Calculate TA
sal = basic + hra  + ta     #Calculate salary = hra +ta
prof_tax = sal * 2/100      #Calculate professional tax i.e 2% of salary
final_sal = sal - prof_tax  #Calculate final salary

print("hra: ",hra,"\nta: ",ta,"\nSalary: ",sal,"\nProfessional Tax: ",prof_tax)  #Display all parameters
print("Final Salary after Professional Tax is: ",final_sal)  #Display Final Pay
print("THANK YOU!") #Greet the user
