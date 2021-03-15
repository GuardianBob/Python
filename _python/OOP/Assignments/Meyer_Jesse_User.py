# For this assignment, we'll add some functionality to the User class:

# make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
# display_user_balance(self) - have this method print the user's name and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $150
# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance 
# by the amount and add that amount to other other_user's balance

class User:		
    def __init__(self, username, email_address):   
        self.name = username			
        self.email = email_address		
        self.account_balance = 0	        
        
    def make_deposit(self, amount):	
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):	
        self.account_balance -= amount
        return self
    def display_user_balance(self):	
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self
    def transfer_money(self, other_user, amount):	
        self.account_balance -= amount        
        other_user.account_balance += amount
        return self
        #-------    ALTERNATE SOLUTION    -----------
        # let's leverage the fact that we have deposit and withdrawal methods that are available to self and other_user
        # since they're both User objects...You don't have to do it this way though
        # other_user.make_deposit(amount) # could also say other_user.account_balance += amount
        # self.make_withdrawal(amount) # could also say self.account_balance -= amount

jesse = User("Jesse", "jesse@mail")
mike = User("Mike", "mike@mail.com")
shea = User("Shea", "shea@mail.com")

jesse.make_deposit(500).make_deposit(200).make_deposit(300).make_withdrawal(100).display_user_balance()

mike.make_deposit(200).make_deposit(800).make_withdrawal(150).make_withdrawal(100).display_user_balance()

shea.make_deposit(1500).make_withdrawal(200).make_withdrawal(100).make_withdrawal(50).display_user_balance()

jesse.transfer_money(shea, 325).display_user_balance()
shea.display_user_balance()

# jesse.make_deposit(500)
# jesse.make_deposit(200)
# jesse.make_deposit(300)
# jesse.make_withdrawal(100)
# jesse.display_user_balance()

# mike.make_deposit(200)
# mike.make_deposit(800)
# mike.make_withdrawal(150)
# mike.make_withdrawal(100)
# mike.display_user_balance()

# shea.make_deposit(1500)
# shea.make_withdrawal(200)
# shea.make_withdrawal(100)
# shea.make_withdrawal(50)
# shea.display_user_balance()

# jesse.transfer_money(shea, 325)
# jesse.display_user_balance()
# shea.display_user_balance()

