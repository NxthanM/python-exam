#this code calculates the net salary which is gross salary by tax rate#

hourly_rate=int(input("Enter the hourly rate for pay (payment per hour): "))
if hourly_rate < 0:
    print("Hourly rate cannot be negative")
    
#prevents using negative numbers#
    
hours_worked=int(input("Enter the number of hours worked: "))
if hours_worked < 0:
    print("Hours worked cannot be negative")
    
tax_rate=0.15

gross_salary = hourly_rate * hours_worked

if gross_salary < 0:
        print("Error, gross salary cannot be negative")
        
net_salary= (1- tax_rate) * gross_salary

print("The net salary is: ", net_salary)




    
