class User:
    # bank_name = "First National Dojo"
    # all_accounts = []

    def __init__(self, cust_num, name, email):
        self.cust_num = cust_num
        self.name = name
        self.email = email
        self.accountList = []
        print(f"// Transaction Begin \\\ \nCustomer account created. \nCustomer Num: {self.cust_num} | Customer Name: {self.name} \nEmail: {self.email} \n\\\ Transaction End   //")
    
    def transaction_footer (self):
        print("\\\ Transaction End   //")

    def createAccount (self, acct_type, acct_num):
        self.acct_type = acct_type        
        print(f"// Transaction Begin \\\ ")
        print(f"Financial account created.  \nCustomer Num: {self.cust_num} | Customer Name: {self.name} | Account Num: {acct_num}")
        my_acct = BankAccount(acct_type, acct_num, balance=0)
        self.accountList.append(my_acct)
        """
        JRF note to self: get some if/else stuff to see if acctNumb already exists, and errror if so. 
        """
        # self.accountList.append(acct_num)
        # BankAccount(acct_type, acct_num, balance=0)
        self.transaction_footer()
        return self
    
    def transaction_header (self, acct_num):
        self.acct_num = acct_num
        print(f"// Transaction Begin \\\ \nCustomer Name: {self.name} | Customer Num: {self.cust_num} | Account Num: {self.acct_num}")

    # a1.make_deposit(987, 20)
    def make_deposit(self, acct_num, amount):
        #self.accountList = []
        # [BankAcct1, BankAcct2]
        for accountObject in self.accountList: 
            if accountObject.acct_num == acct_num:
                self.transaction_header(acct_num)
                print(f'found account {acct_num}, depositing ${amount}')
                accountObject.deposit(acct_num, amount)
                self.transaction_footer()
            """
            JRF note to self: need an else statement here! 
            """
            # else: 
            #     print("Account Number provided in invalid.")
        # self.acct_num = acct_num
        
        # print(f"self.account.balance: {self.account.balance}")
        # print('looking at the user account(s)')
        # print(self.account.acct_type)
        # print(self.account.acct_num)
        
        
        return self
class BankAccount:
    # accounts = []
    def __init__(self, acct_type, acct_num, balance):
        self.acct_type = acct_type
        self.acct_num = acct_num
        if acct_type == "Checking": 
            x = 0.02
        else: 
            x = 0.03
        self.int_rate = x
        self.balance = balance
        self.int_rate_display = self.int_rate * 100
        # print(f"Account Type: {self.acct_type}")
        print(f"Current balance is ${self.balance} with a current interest rate of {self.int_rate_display}%.")
        # return None
    def display_account_info (self, acct_num):
        self.acct_num = acct_num
        # print("this is the display_account_info funct")
        print(f"Account Balance: ${self.balance}")
        # return self    
    #acct_num = 123
    def deposit (self, acct_num, amount): 
        ## if self.acct_num = acct_num: do somethin
        self.balance += amount
        print(f"Deposit accepted: ${amount}.")
        self.display_account_info(acct_num)

        # if self.acct_num == acct_num:
        #     self.balance += amount
        #     print(f"Deposit accepted: ${amount}.")
        #     self.display_account_info(acct_num)
        # else: 
        #     print("Account Number provided in invalid.")
        # self.acct_num = acct_num
        # print(f"example text Account Class self.acct_num: {self.acct_num}")

        return self

"""
    def withdraw (self, amount):
        if self.balance < amount:
            self.old_balance = self.balance
            self.balance -= 5
            print(f"Insufficient funds.  You tried to withdraw ${amount} but your balance was only ${self.old_balance}.  For even attempting that, we just charged you a completely unjustifiable $5 fee... and you cant do jack about it.")
            self.display_account_info()
            # print(f"Balance: ${self.balance}")
        else: 
            self.balance -= amount
            print(f"Withdrawl completed: ${amount} ")
            self.display_account_info()
            # print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.int_added = self.balance * self.int_rate
            self.balance =  self.int_added + self.balance
            print(f"Interest yield added to account in the amount: ${self.int_added}.")
            self.display_account_info()
            # print(f"Balance: ${self.balance}")
        else: 
            print(f"No interest yield payment: account balance less than or equal to zero.")
            self.display_account_info()
            # print(f"Balance: ${self.balance}")
        return self
"""


"""
    @classmethod
    def print_all_accounts(cls):
        print("List of all account balances:::::::::::::::::::")
        for x in cls.accounts:
            x.display_account_info()
    
    @classmethod
    def all_balances(cls):
        sum = 0
        for account in cls.all_accounts:
            sum += account.balance
        print(sum)

"""

# BankAccount.print_all_accounts()

a1 = User("ABC", "Lucky Day", "lucky@3amigos.com")
# a2 = User("DEF", "Dusty Bottoms", "dusty@3amigos.com")
# a3 = User("GHI", "Ned Nederlander", "ned@3amigos.com")

a1.createAccount("Checking", 123)
# print(a1.account)
a1.createAccount("Savings", 987)

# print(a1.accountList)

a1.make_deposit(123, 1)
a1.make_deposit(987, 100)
a1.make_deposit(123, 2)
a1.make_deposit(123, 2)
a1.make_deposit(987, 200)
a1.make_deposit(987, 300)

# print(a1.accountList[0].balance)

for account in a1.accountList:
    print(f'This is my account type: {account.acct_type}')
    print(f'This is my account number: {account.acct_num}')
    print(f'This is my account balance: {account.balance}')
    print('============================================')





# .make_deposit(123, 200).make_deposit(123, 300)
# # a1.make_deposit(987, 2000)
# a1.make_deposit(987, 3000)
# a1.make_deposit(123, 2)
# a1.make_deposit(123, 3)
# .make_deposit(123, 200).make_deposit(123, 300)
# .make_deposit(43).make_deposit(53).make_withdrawal(130).yield_interest().display_user_balance()

# a1.account.deposit(987, 5000)


"""
    def make_withdrawal(self, amount):	# takes an argument that is the amount of the deposit
        # self.account_balance += amount	# the specific user's account increases by the amount of the value received
        # above replaced with below... work in progress
        # self.account = BankAccount(acct_num = 123, int_rate=0.05, balance=0)
        self.transaction_header()
        self.account.withdraw(amount)
        self.transaction_footer()
        return self

    # def make_withdrawal(self, amount):
    # # have this method decrease the user's balance by the amount specified
    #     self.account_balance -= amount
    #     return self

    def display_user_balance(self): 
        # self.balance_display = print(f"User: {self.name}, Balance: ${self.account_balance}")
        # above replaced by below
        self.transaction_header()
        self.account.display_account_info()
        self.transaction_footer()
        return self
    
    def yield_interest(self): 
        # self.balance_display = print(f"User: {self.name}, Balance: ${self.account_balance}")
        # above replaced by below
        self.transaction_header()
        self.account.yield_interest()
        self.transaction_footer()
        return self


    def transfer_money(self, other_user, amount): 
        self.account_balance -= amount
        other_user.account_balance += amount
        self.balance_display = print(f"User: {self.name}, Balance: ${self.account_balance}")
        other_user.balance_display = print(f"User: {other_user.name}, Balance: ${other_user.account_balance}")
        return self
    #have this method decrease the user's balance by the amount and add that amount to other other_user's balance
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