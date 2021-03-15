class BankAccount:
	def __init__(self, int_rate=.01, balance=0):
		self.interest = int_rate
		self.balance = balance
		
	def deposit(self, amount):
		self.balance += amount
		return self

	def withdraw(self, amount):
		# self.balance -= amount    <---------Original code
# ---------- Bank Acct solution code below: ---------------- 
		if self.balance >= amount:
			self.balance -= amount
		else:
			self.balance -= 5
			print("Insufficient Funds: Charging a $5 fee")
#----------- End of Bank solution code ----------------------
		return self

	def display_account_info(self):
		print(f"Balance: {self.balance}")
		return self

	def yield_interest(self):
		if self.balance > 0:
			self.balance = (self.balance * self.interest) + self.balance
		return self

class User:		
	def __init__(self, username, email_address):   
		self.name = username			
		self.email = email_address		
		self.account = BankAccount(.02, 0)
		
	def make_deposit(self, amount):	
		self.account.deposit(amount)
		return self
	def make_withdrawal(self, amount):	
		self.account.withdraw(amount)
		return self
	def display_user_balance(self):	
		print(f"User: {self.name}, Balance: {self.account.balance}")
		return self
	def transfer_money(self, other_user, amount):	
		self.account.withdraw(amount)        
		other_user.account.deposit(amount)
		return self	

jesse = User("Jesse", "jesse@mail")
mike = User("Mike", "mike@mail.com")
shea = User("Shea", "shea@mail.com")

jesse.make_deposit(500).make_deposit(200).make_deposit(300).make_withdrawal(100).display_user_balance()

mike.make_deposit(200).make_deposit(800).make_withdrawal(150).make_withdrawal(100).display_user_balance()

shea.make_deposit(1500).make_withdrawal(200).make_withdrawal(100).make_withdrawal(50).display_user_balance()

jesse.transfer_money(shea, 325).display_user_balance()
shea.display_user_balance()

