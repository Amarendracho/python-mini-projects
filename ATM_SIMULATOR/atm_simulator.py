
initial_balance = 10000

def check_balance():
    return initial_balance

def deposit():
    global initial_balance
    amount = int(input("Enter deposit amount: $"))

    if amount <= 0:
        print("Deposit amount must be greater than 0")
        return

    initial_balance += amount
    print(f"Deposit successful. Available balance = ${initial_balance}")

def withdrew():
    global initial_balance
    amount = int(input("Enter withdrew amount: $"))

    if amount <= 0:
        print("Withdrew amount must be greater than 0")
        return

    if amount <= initial_balance:
        initial_balance -= amount
        print(f"Withdrew Successful. Available balance = ${initial_balance}")
    else:
        print(f"Withdrew Failed. insufficient funds. balance = ${initial_balance}")

def bye():
    print("Thank you for banking with us 😊")


def atm_simulator():
    while True:
        userinput = input(
            "How can i help you today? :) \n"
            "1) Check Balance \n"
            "2) Deposit \n"
            "3) Withdrew \n"
            "4) Bye\n"
            "Enter your choice : ").strip().lower()

        if userinput in ["1","Check Balance","balance"]:
            print(f"Your balance is: ${check_balance()}")
        elif userinput in ["2","Deposit","deposit"]:
            deposit()
        elif userinput in ["3","withdrew"]:
            withdrew()
        elif userinput in ["4","bye","exit"]:
            bye()
            return
        else:
            print("Invalid option. Please try again.")

atm_simulator()

