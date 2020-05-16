# Let's continue working with classes by creating 
# a Bank Account 
# that accepts a users name and contains a starting
# balance of 0. 
# Bank accounts have the ability to deposit and 
# withdrawl funds in 
# addition to checking if the balance is 
# positive and if the withdrawl 
# amount is enough. 
# Once you've created the class,
#  complete the requirements below.

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
# continue shopping or
# to close their cart

#from helpers import Account

name = input("Hello, please enter your name: ")

initial = int(input('Please enter your initial deposit: '))

account = []

account.append(initial)

shopping = ''

while shopping != 'q':
    print("""Choose an item or deposit more funds")
    1. Buy shirt for $100
    2. Buy shoes for $200
    3. Buy pants for $40
    4. Deposit more funds
    """)

    choice = int(input("Enter your choice: "))

    if choice == 1:
        account.append(100)
        print(sum(account))

    elif choice == 2:
        print('choose 2')
    elif choice == 3:
        print('choose 3')
    elif choice == 4:
        print("choose 4")
    
    shopping = input("Hit any key to continue shopping or press q to quit: ")
