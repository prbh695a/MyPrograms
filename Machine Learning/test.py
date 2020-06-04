balance = 0
oldpassw = "old"
while (-1):
    print("1.Cash Withdraw")
    print("2.Cash credit")
    print("3.Change password")
    print("4.Exit")
    inp = int(input("Enter the option: "))
    if (inp == 4):
        break
    if (inp == 1):
        amount = int(input("Enter the amount to withdraw: "))
        if (amount < balance):
            balance = balance - amount
            print("The current balance is:", balance)
        else:
            print("The current balance is low, cannot withdraw", balance)
    if (inp == 2):
        amount = int(input("Enter the amount to credit: "))
        balance = balance + amount
        print("The current balance is:", balance)
    if (inp == 3):
        passw = input("Enter the old password:")
        if (passw == oldpassw):
            npassw = input("Enter the new password: ")
            oldpassw = npassw
            print("The password has been successfully changed")
        else:
            print("Please enter correct password!!!")




