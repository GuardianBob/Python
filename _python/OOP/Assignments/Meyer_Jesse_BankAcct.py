class BankAccount:
	def __init__(self, int_rate=.01, balance=0):
		self.interest = int_rate
		self.balance = balance
        # don't forget to add some default values for these parameters!
		# # your code here! (remember, this is where we specify the attributes for our class)
        # don't worry about user info here; we'll involve the User class soon
		
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

acct1 = BankAccount(balance=100)
acct2 = BankAccount()

acct1.deposit(500).deposit(800).deposit(1000).withdraw(600).yield_interest().display_account_info()
acct2.deposit(800).deposit(1000).withdraw(200).withdraw(100).withdraw(500).withdraw(200).yield_interest().display_account_info()

