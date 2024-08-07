import time

print("Insert ur card")
time.sleep(1)

password=1234
bal=5000
transaction = []

pin=int(input("enter pin number:\n"))
if pin==password:
    while True:
        print("""
                MAIN MENU
            1.bal check
            2.withdraw
            3.deposit
            4.pin change
            5.transaction history
            6.exit
              
            """)
        
        try:
            option=int(input("enter ur option:\n"))
        except:
            print("enter valid option\n")
            
        if option==1:
            print(f"ur current bal is {bal}")
            
        if option==2:
            withdraw=int(input("enter amount to withdraw\n"))
            #the user should have minimum bal of 500
            if (bal>500 and bal-withdraw>=500):
                bal=bal-withdraw
                transaction.append(f"Withdraw: {withdraw}")
                print(f"{withdraw} amount is debited")
                print(f"ur current bal is {bal}")  
            else:
                print(f"withdraw will reduce minimum bal ")  

        if option==3:
            deposit=int(input("enter amount to deposit\n"))
            bal=bal+deposit
            transaction.append(f"Deposit: {deposit}")
            print(f"{deposit} amount is credited")
            print(f"ur current bal is {bal}") 
            
        if option==4:
            try:
                new_pin = int(input("Enter new PIN:\n"))
                if 1000 <= new_pin <= 9999:
                    password = new_pin
                    print("PIN successfully changed.")
                else:
                    print("PIN must be a 4-digit number.")
            except:
                print("Invalid input. Please enter a valid number.")
            

        if option==5:
            if transaction:
                print("Transaction History:")
                for tr in transaction:
                    print(tr)
            else:
                print("No transaction")

        if option==6:
            print("exiting")
            break       
else:
    print("wrong pin! try again")

