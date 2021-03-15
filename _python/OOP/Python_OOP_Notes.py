# Classes - Objects
#   Attributes - Describe the Class
#   Methods - What the class can do
#   Attributes are defined in the __init__ 
#   Attributes: Characteristics shared by all instances of the class type.
#   Methods: Actions that an object can perform.  They are just functions that belong to a class.
#       A user, for example, should be able to make a deposit or a withdrawal, or maybe send money to another user.
#     !!!!!!  the first parameter of every method within a class should be self
#   Chaining - Methods can be chained together.  Ex:
#       user.make_deposit(100).make_deposit(200).make_deposit(100).display_balance()  <--- this will deposit 400 and display the balance afterwards
#    !!!!!!!!!  Methods must return self for chaining to work!!
#    !!!!!!!!!  When importing a Class from another module, it MUST be imported as:  from file_name import class_name 




#================= Class Buildout Example =============================
class User:		# declare a class and give it name User
    def __init__(self, username, email_address):    # now our method has 2 parameters!
        # self.name = "Michael"         # Causes every new instance to start with the name attr as "Michael"
        self.name = username			# and we use the values passed in to set the name attribute
        self.email = email_address		# and the email attribute
        self.account_balance = 0		# the account balance is set to $0, so no need for a third parameter
        # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received
        return self   #<-------------THIS MUST BE INCLUDED IN ORDER TO BE ABLE TO CHAIN METHODS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def make_withdrawal(self, amount):	
        self.account_balance -= amount
    def display_user_balance(self):	
        print(f"User: {self.name}, Balance: {self.account_balance}")
    def transfer_money(self, other_user, amount):	
        self.account_balance -= amount
        other_user.account_balance += amount
        #-------    ALTERNATE SOLUTION    -----------
        # let's leverage the fact that we have deposit and withdrawal methods that are available to self and other_user
        # since they're both User objects...You don't have to do it this way though
        # other_user.make_deposit(amount) # could also say other_user.account_balance += amount
        # self.make_withdrawal(amount) # could also say self.account_balance -= amount

#    Created before changing the name attribute above.
michael = User()
anna = User()      
print(anna.name)  #     Printed "Michael" because the User class name attribute was set as "Michael" before we changed it

anna.name = "Anna"  #   Sets value for the "anna" instance of the User class

guido = User("Guido van Rossum", "guido@python.com")  #     After changing name attr to username above we are required to enter arguments for any
#                                                             undefined attributes of the User class
monty = User("Monty Python", "monty@python.com")
print(guido.name)	# output: Guido van Rossum
print(monty.name)	# output: Monty Python

#   Once the "make_deposit" method is defined, the following functions can be called:
guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(50)
print(guido.account_balance)	# output: 300
print(monty.account_balance)	# output: 50


#=======================================================================
