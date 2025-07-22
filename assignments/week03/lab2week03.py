# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("x"*20)
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit\n")
        print("x"*20)
        choice = input("Choose option: ")
        
        # Complete the menu logic here
        # Your code here:
        if choice == "1":
            print("Balance = ",balance)

        elif choice == "2":
            withdraw = float(input("How much you want to withdraw?: "))
            if withdraw > 0 and balance > withdraw:
                print("Withdraw = ",withdraw)
                print("Your balance now = ",balance - withdraw)
                balance = balance - withdraw
            else:
                print("can not withdraw less then zero!")
            
        elif choice =="3":
            deposite = float(input("How much you want to Deposite?: "))
            if deposite > 0:
                print("Deposite = ",deposite)
                print("Your balance now =",balance + deposite)
                balance = balance - deposite
            else:
                print("can not deposite less then zero!")

        elif choice =="4":
            break
else:
    print("Invalid PIN")
