class Account:
  def __init__(self,name,bank,number,password):
    self.name = name
    self.bank = bank
    self.number = number
    self.password = password
    self.balance = 0

  

class ATM:
  def __init__(self,bank):
    self.bank = bank
    self.accounts = []
    self.currentaccount = None

  def showhome(self):
    working = True
    while working:
      print("Welcome to the ATM")
    option = int(input("What do you want to do?\n(1) open account\n(2) load account\n(3) deposit\n (4) withdraw\n check balance\n(5) exit "))
      if option == 1:
        self.addaccount()
      elif option == 2:
        self.loadaccount()
      elif option == 3:
        self.deposit()
      elif option == 4:
        self.withdraw()
      elif option == 5:
        self.exit()
      else:
        print("did not understand. Please try again")
      return 
  
  def addaccount(self):
    name = input("Please enter your name ")
    bank = input("Please enter the bank ")
    number = int(input("Please enter your account number "))
    password = input("Please enter your account password ")
    self.accounts.append(Account(name,bank,number,password))
  return True

  def loadaccount(self):
    name = input("Please enter the name on the account to load ")
    for testaccount in self.accounts:
      if testaccount.name == name:
        self.account = testaccount
    

  def deposit(): self.balace += amount to deposit 