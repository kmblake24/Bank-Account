# Write an application that:
# Prompts a user for their name
# Prompts a user for an initial deposit

# Opens an account for the user, accepting
# their initial deposit

# Prompts them to shop at an online store with three
# potential items to purchase and an option to deposit 
# more funds

# Outputs user can't afford an item when they're 
# account is low

# After each purchase, prompts a user to
# continue shopping or to close their cart

from helpers import BankAccount

name = input("Hello, please enter your name: ")

initial = int(input('Please enter your initial deposit: '))

bank = BankAccount(name)
bank.make_deposit(initial)

shopping = ''
while shopping != 'q':
    print("""Choose an item or deposit more funds
    1. Buy shirt for $100
    2. Buy shoes for $200
    3. Buy pants for $40
    4. Deposit more funds
    5. Check Balance
    """)

    choice = int(input("Enter your choice: "))
    amount = 0

    if choice == 1:
        amount = 100
        bank.withdraw(amount)
        print(f'Your balance is {bank.check_bal()}')
    elif choice == 2:
        amount = 200
        bank.withdraw(amount)
        print(f'Your balance is {bank.check_bal()}')
    elif choice == 3:
        amount = 40
        bank.withdraw(amount)
        print(f'Your balance is {bank.check_bal()}')
    elif choice == 4:
        amount = int(input("Enter how much you want to deposit: "))
        bank.make_deposit(amount)
        print(f'Your balance is {bank.check_bal()}')
    elif choice == 5:
        print(f'Your balance is {bank.check_bal()}')

    shopping = input("Hit any key to continue shopping or press q to quit: ")
