
balance=0
Deposit_val=int(input("Enter the amount you are depositting: "))
balance_val= balance + Deposit_val

withdraw_val=int(input("Enter the amount you would like to withdraw: "))
Current_balance= balance_val - withdraw_val
if withdraw_val > balance_val :
    print(" You cannot withdraw more money than your balance")
elif withdraw_val < balance_val : print ("You are withdrawing $", withdraw_val )

Acc_no= 123456789
print ("Statement for Account number :", Acc_no, "is shown below") 
print ( "Deposit amount $", Deposit_val)
print ( "Withrawal amount $", withdraw_val)
print ( "Current amount $", Current_balance)
