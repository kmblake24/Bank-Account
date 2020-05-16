# Class will accept a username and balance

# The __init__ method serves as the constructor for our class, 
# allowing us to define attributes and the initial state of each car that gets made.

# self - represents the instance of the class; by using self you can access
# the attributes of the class; self only affects the class being used; not all instances of the
# class

# for name - the name will be passed through the class
# class Bank_Account instantiates the class - you will need to pass the name here
# will do class Bank_Account(self, object)

# predeteming every balance will start at 0
# have to pass in object b/c the name will be passed into the class

class BankAccount(object):  
    def __init__(self, object):
        self.name = object
        self.balance = 0
    # above is the constructor

# test - see the attributes, see if you can pass a name
# we intended our object to be a name; so pass it in
# use ._dict_ to see the dictionaries attributes

# bank = BankAccount("Kyle")
# print(bank.__dict__)
# outputs: {'name': 'Kyle', 'balance': 0}


