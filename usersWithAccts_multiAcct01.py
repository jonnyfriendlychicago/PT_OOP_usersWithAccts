"""There are two classes in this script: Customer and BankAccount.  """

class Customer:
    custAccountList = [] # this list gets created upon script run; THEN, we append Customer objects into it, for review/display/validation later. zi9546

    """ below methods are mere print text, to diplay in terminal, for viewer ease.  These two methods are called upon by all downstread methods """
    def transactionHeader(self):
        print("\\\Transaction Begin ---------------------- \\\ ")

    def classTransactionHeader():
        print("\\\Transaction Begin ---------------------- \\\ ")

    def transactionFooter (self):
        print("// ---------------------- Transaction End  //")

    def classTransactionFooter():
        print("// ---------------------- Transaction End  //")

    """below method is invoked by various transactions.  It basically prints the type of transaction that is being initiated."""
    ## I'm assuming that i'll want to change these words/format/etc 1,000 times.  having the text as a repeated call resolve that. 
    def transTypeAffirmation (self, transType):
        print(f"{transType} initiated.") 

    """below method prints vital elements of the customer object.  This is invoked by virtually all downstream calls.  
    It affirms which customer is being affected by an activity (like a deposit) """
    def customerAffirmation (self):
        print(f"Customer Num: {self.cust_num} | Customer Name: {self.name} | Email: {self.email}")
    
    """ below method initiates the customerAccount object.  read comments therein for further detail"""
    def __init__(self, cust_num, name, email):
        # JRF note to self: here we should have some error checking logic: if cust_num or email already exists, send error message.  this will require reactivation of the "All_accounts = []" list, I think
        self.cust_num = cust_num
        self.name = name
        self.email = email
        # jrf note to self: here create a bunch of fields for the customer, and set to "", to be populated with downstream calls. 
        """ this "finAccountList" list below is SUPER IMPORTANT: it's what enables the entire organization of separate/distinct/callable bank accounts"""
        self.finAccountList = [] # this shall be an list of all **account** objects (dictionaries) that shall be created/associated to this customer object.  list is on the object, not on the overall class
        self.transactionHeader()
        # transType = "New Customer Account" # this code is fine, but not what I want it to be for right now, so leave out for now.
        # self.transTypeAffirmation(transType) 
        Customer.custAccountList.append(self)
        print(f"New Customer Account created.") # this msg affirms in terminal that attempt was successful. 
        self.customerAffirmation()
        self.transactionFooter()
    

    @classmethod
    def displayAllCustomerAccount(cls):
        cls.classTransactionHeader()
        for account in cls.custAccountList:
            print(f"yo' valuuu: {account.name}")
            # account.display_account_info()
        
        cls.classTransactionFooter()

    """ below displays customer info and various views of the customer accounts"""
    def displayAllFinancialAccount (self): 
        self.transactionHeader()
        print(f"Customer-plus-accts summary")
        self.customerAffirmation()
        
        """ below will print out a dictionary-format of the dictionary items in finAccountList"""
        print(f"Printing the Dictionary")
        for accountObject in self.finAccountList:     
            print(f"{(accountObject.__dict__)}")  
        
        """below works to print out known variables by specifically calling for them"""
        print(f"printing dict objects, value-by-value")
        print(f"Customer Account Summary:")
        self.customerAffirmation()
        print(f"Financial Accounts:")
        for accountObject in self.finAccountList: 
            print(f" Account Num: {accountObject.acct_num}\n  Account Type: {accountObject.acct_type}\n  Interest Rate: {accountObject.int_rate_display}%\n  Current Balance: ${accountObject.balance}") 

        """ below is attempt to iterate through above... and it works!  puts them all in a vert list, but it works!"""
        print(f"Iterating thru the object dictionaries")
        for accountObject in self.finAccountList: 
            print (f"Account Details:")
            x = (accountObject.__dict__)
            for k,v in x.items():
                print (f"   {k}: {v}")
        self.transactionFooter()

    """below method initiates the init method on the BankAccount class, thereby creating a financialAccount object, specifically joined to a Customer account object.  it is invoked by this call: 
    a1.createFinancialAccount("Checking", 123)    """
    def createFinancialAccount (self, acct_type, acct_num):
        self.acct_type = acct_type # sets the internal variable       
        """
        JRF note to self: get some if/else stuff to see if acctNumb already exists, and errror if so. also, if type is not checking or savings, that should error also.  
        """
        self.transactionHeader()
        transType = "New Financial Account"
        self.transTypeAffirmation(transType)
        self.customerAffirmation()
        # my_acct = BankAccount(acct_type, acct_num, balance=0) # establishes 'my_acct' as var for class-init function for BankAccount 
        my_acct = BankAccount(acct_type, acct_num) # establishes 'my_acct' as var for class-init function for BankAccount 
        self.finAccountList.append(my_acct)    # accomplishes two things in one action: 
                                                #(1) this adds the about-to-be-created instance/object to the finAccountList list that exists for this customer acct 
                                                #(2) inherently runs that class-init function, using the var pushed into in from the call.  see init function in the BankAccount class code further in script. 
        self.transactionFooter()
        return self

    """below method does not create an object; rather, it initiates the deposit method that exists within the BankAccount class.  see bankAccount class code further in script. 
    """
    def make_deposit(self, acct_num, amount):
        #self.finAccountList = []
        # [BankAcct1, BankAcct2]
        displayAmount = "{:,}".format(amount) # this is a display variable, so that amounts are displayed with commas.  do this throughout the script, not just here. 
        self.transactionHeader()
        transType = "New Deposit"
        self.transTypeAffirmation(transType)
        accountFound = False # accountFound is an internal variable, set to False at start.  In other words, we start by saying the account can't be found, then update the var if/when it is found
        for accountObject in self.finAccountList: 
            if accountObject.acct_num == acct_num:
                # JRF note to self: would like to have additional logic above that validates both the Customer as well as the account number, but not 100% sure that's needed
                accountFound = True # we found the account!  so, we set the var = True.  that way, the "not found" error message never gets invoked, see couple lines down. 
                self.customerAffirmation()
                """ below is what makes the magic happen; it's saying: run the deposit method ON THIS accountObject"""
                accountObject.deposit(acct_num, amount)
        if accountFound == False: #this only occurs if no accountObject located in the forLoop above
            print(f"Deposit failed: cannot locate account number: {acct_num}.  ${displayAmount} deposit has not occurred.")
        # print(f"below is print(self.finAccountList)")
        # print(self.finAccountList)
        self.transactionFooter()
        return self

class BankAccount:
    # accounts = []
    # def __init__(self, acct_type, acct_num, balance):
    
    """ below method invoked by all transactions.  affirms the acct num and type that transactions are affecting"""
    def accountAffirmation (self, acct_num):
        self.acct_num = acct_num
        print(f"Account Number: {self.acct_num} | Account Type: {self.acct_type}")
    
    """ below is invoked by the account creation method, and can also be invoked individually by an accountbalanceLookup method, which I will build later. """
    def accountDetails (self, acct_num):
        self.acct_num = acct_num
        print(f"Current balance is ${self.balance} with a current interest rate of {self.int_rate_display}%.")
    
    """ below is invoked by the deposit/withdrawl/etc method """
    def accountBalance (self, acct_num):
        self.acct_num = acct_num
        print(f"Account Balance: ${self.balance}")
        
    """ below init method creates the bankAccount object.  it is called by a method in the Customer class."""
    def __init__(self, acct_type, acct_num):
        self.acct_type = acct_type
        self.acct_num = acct_num
        self.balance = 0 # all finAccounts objects start with a balance of zero.  that goes up/down when finTrans start occurring
        if acct_type == "Checking": #setting the interest rate depending on account type.  Could this also be done with a parent/child set-up??  maybe try that later. 
            self.int_rate = 0.02
        else: 
            self.int_rate = 0.03
        self.int_rate_display = self.int_rate * 100 # this is purely for cosmetics in the terminal window
        print("New Financial Account created.") # affirms that the attemped account creation occurred successfull
        self.accountAffirmation (acct_num) # see method above
        self.accountDetails(acct_num)  # see method above
        # return None
    
    def deposit (self, acct_num, amount): 
        self.balance += amount
        self.accountAffirmation(acct_num)
        print(f"Deposit accepted: ${amount}.")
        self.accountBalance(acct_num)
        return self

# BankAccount.print_all_accounts()

a1 = Customer("ABC", "Lucky Day", "lucky@3amigos.com")
a1.createFinancialAccount("Checking", 123)
a1.make_deposit(123, 1)
a1.make_deposit(123, 2)
a1.createFinancialAccount("Savings", 987)
a1.make_deposit(987, 100)
a1.make_deposit(313, 10_000_000) #this account doesn't exist / won't exist.  this shows what happens when you send an acct_num that hasn't been created yet. 

a2 = Customer("DEF", "Dusty Bottoms", "dusty@3amigos.com")
a2.createFinancialAccount("Savings", 924)

a1.displayAllFinancialAccount()

Customer.displayAllCustomerAccount()

"""

a2.createFinancialAccount("Checking", 219) # this big list of accounts shows how you can create wide range of accounts. 

a2.createFinancialAccount("Savings", 376)
a2.createFinancialAccount("Checking", 773)
a2.createFinancialAccount("Checking", 847)
a2.make_deposit(219, 1000)
a2.make_deposit(219, 5000)



a3 = Customer("GHI", "Ned Nederlander", "ned@3amigos.com")
# no other tests for a3 yet, we good for now.
"""

# print(Customer.finAccountList)
"""
All of below is more stuff I want to get back to!!!!!!!! - JRF 2022.02.18

"""


"""
    def withdraw (self, amount):
        if self.balance < amount:
            self.old_balance = self.balance
            self.balance -= 5
            print(f"Insufficient funds.  You tried to withdraw ${amount} but your balance was only ${self.old_balance}.  For even attempting that, we just charged you a completely unjustifiable $5 fee... and you cant do jack about it.")
            self.accountBalance()
            # print(f"Balance: ${self.balance}")
        else: 
            self.balance -= amount
            print(f"Withdrawl completed: ${amount} ")
            self.accountBalance()
            # print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.int_added = self.balance * self.int_rate
            self.balance =  self.int_added + self.balance
            print(f"Interest yield added to account in the amount: ${self.int_added}.")
            self.accountBalance()
            # print(f"Balance: ${self.balance}")
        else: 
            print(f"No interest yield payment: account balance less than or equal to zero.")
            self.accountBalance()
            # print(f"Balance: ${self.balance}")
        return self
"""


"""
    @classmethod
    def print_all_accounts(cls):
        print("List of all account balances:::::::::::::::::::")
        for x in cls.accounts:
            x.accountBalance()
    
    @classmethod
    def all_balances(cls):
        sum = 0
        for account in cls.all_accounts:
            sum += account.balance
        print(sum)

"""


"""
# print(a1.account)


# print(a1.finAccountList)
"""




# a1.make_deposit(987, 200)







"""
# print(a1.finAccountList[0].balance)

for account in a1.finAccountList:
    print(f'This is my account type: {account.acct_type}')
    print(f'This is my account number: {account.acct_num}')
    print(f'This is my account balance: {account.balance}')
    print('============================================')

"""



# .make_deposit(123, 200).make_deposit(123, 300)
# # a1.make_deposit(987, 2000)
# a1.make_deposit(987, 3000)
# a1.make_deposit(123, 2)
# a1.make_deposit(123, 3)
# .make_deposit(123, 200).make_deposit(123, 300)
# .make_deposit(43).make_deposit(53).make_withdrawal(130).yield_interest().display_Customer_balance()

# a1.account.deposit(987, 5000)


"""
    def make_withdrawal(self, amount):	# takes an argument that is the amount of the deposit
        # self.account_balance += amount	# the specific Customer's account increases by the amount of the value received
        # above replaced with below... work in progress
        # self.account = BankAccount(acct_num = 123, int_rate=0.05, balance=0)
        self.customerAffirmation()
        self.account.withdraw(amount)
        self.transactionFooter()
        return self

    # def make_withdrawal(self, amount):
    # # have this method decrease the Customer's balance by the amount specified
    #     self.account_balance -= amount
    #     return self

    def display_Customer_balance(self): 
        # self.balance_display = print(f"Customer: {self.name}, Balance: ${self.account_balance}")
        # above replaced by below
        self.customerAffirmation()
        self.account.accountBalance()
        self.transactionFooter()
        return self
    
    def yield_interest(self): 
        # self.balance_display = print(f"Customer: {self.name}, Balance: ${self.account_balance}")
        # above replaced by below
        self.customerAffirmation()
        self.account.yield_interest()
        self.transactionFooter()
        return self


    def transfer_money(self, other_Customer, amount): 
        self.account_balance -= amount
        other_Customer.account_balance += amount
        self.balance_display = print(f"Customer: {self.name}, Balance: ${self.account_balance}")
        other_Customer.balance_display = print(f"Customer: {other_Customer.name}, Balance: ${other_Customer.account_balance}")
        return self
    #have this method decrease the Customer's balance by the amount and add that amount to other other_Customer's balance
"""   

"""
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
        print(cls.bank_name)
    
    @classmethod
    def all_balances(cls):
        sum = 0
        for account in cls.all_accounts:
            sum += account.balance
        return sum
"""