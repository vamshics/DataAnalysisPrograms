import sys
class Customer:
	bankName='DURGABANK'

	def __init__(self,name,balance=0.0):
		self.name=name
		self.balance=balance
	
	def deposit(self,amount):
		self.balance=self.balance+amount
		print('Hello After Deposit Balance:',self.balance)
	
	def withdraw(self,amount):
		if amount>self.balance:
			print('Sorry..Insufficient Funds cannot perform this operation')
			sys.exit()
		else:
			self.balance=self.balance-amount
			print("Hello After withdraw Balance:",self.balance)

	
print("Welcome to Python ",Customer.bankName)
name=input('Enter Your Name:')
c1=Customer(name)
print("Hello",c1.name,"Your Account got Created")
while True:
	print('D-Deposit\nW-WithDraw\nE-Exit')
	option=input('Choose Your Option:')
	if option =='D' or option =='d':
		amount=float(input('Enter Amount:'))
		c1.deposit(amount)
	elif option=='W' or option=='w':
		amount=float(input('Enter amount to withdraw:'))
		c1.withdraw(amount)
	elif option=='E' or option=='e':
		print('Thanks for Banking')
		sys.exit()
	else:
		print('Invalid option..plz choose valid option')
