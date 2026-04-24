import random,msvcrt
print("WELCOME TO THE ATM XYZ BANK")
print("PLEASE PUT YOUR CARD IN")
'''
print(" 1.Check balance \n 2.Deposit \n 3.Withdraw")
choice=int(input("Choose your option(1/2/3)"))
card_balance=random.randint(100,10000000)
def balance():
    for i in range(1,4):
        print("."*i,end='\r')
        time.sleep(2)
    print("YOUR BALANCE IS : Rs",card_balance)
    thankyou()
def withdraw():
    amount=float(input("Withdraw Rs:" ))
    print("DO NOT TAKE YOUR CARD OUT DURING THE PROCESS")
    for i in range(1,4):
        print("."*i,end='\r')
        time.sleep(2)
    print("YOUR CASH HAS BEEN WITHDRAWN.\nWould you like to see balance?(Y/N) ")
    c=input()
    if c=='Y':
        print("Balance is Rs",card_balance-amount)
        thankyou()
    else:
        thankyou()
def thankyou():
    print("Have a great day!")
def deposit():
    deposit=float(input("How much do you want to deposit? Rs"))
    for i in range(1,4):
        print("."*i,end='\r')
        time.sleep(2)
    print("Your amount has been deposited. \nYour new balance is Rs",card_balance+deposit)
    thankyou()
if choice==1:
    balance()
elif choice==2:
    deposit()
elif choice==3:
    withdraw()
else:
    print("Invalid choice")'''


def pinnum():
    pin = ""
    print("Enter PIN: ", end="")

    while True:
        x = msvcrt.getch().decode()   

        if x == '\r':
            break

        elif x == '\x08':
            if pin != "":
                pin = pin[:-1]       
                print('\b \b', end='')

        elif x.isdigit():
            pin += x                 
            print("*", end='')

pinnum()