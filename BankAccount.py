import time

class BankAccount(object):
  balance = 0
  def __init__(self, name):
    self.name = name
    
  def __repr__(self):
    return ("%s's account. Balance %.2f") % (self.name, self.balance)
  
  def show_balance(self):
    print ("Balance %.2f") % (self.balance)
    
  def deposit(self, amount):
    if amount <= 0:
      print ("Amount needs to be bigger than 0.")
      return
    else:
      print ("Deposited %.2f") % (self.balance)
      self.balance += amount
      self.show_balance()
      
  def withdraw(self, amount):
    if amount > self.balance:
      print ("Not enough balance.")
    ###########Problem starts from here#############
      time.sleep(1)
      answer = raw_input("Would you like to take a loan?: ")
    elif answer == "Yes":
      print ("You can take a loan of 5000$ with %5 interest.")
      answer2 = raw_input("Do you wish to proceed?")
    elif answer2 == "Yes"
      print ("Withdrawing %.2f") % (self.balance)
    ##########Ends here############# 
    else:
      print ("Withdrawing %.2f") % (self.balance)
      self.balance -= amount
      self.show_balance()

my_account = BankAccount("21-Savage")
print my_account
my_account.show_balance()
my_account.deposit(20000)
my_account.withdraw(1000)
print my_account
