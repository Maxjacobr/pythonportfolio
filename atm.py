#Max Rubenstein
#ATM

balance = 0

def deposit(amount):
    global balance
    balance += amount
    print(f"Deposited {amount}")
def withdraw(amount):
    global balance
    balance -= amount
    print(f"Withdrew {amount}")
def total():
    print(f"Balance = {balance}")
deposit(50)
withdraw(30)
total()
