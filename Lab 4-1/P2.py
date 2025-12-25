class BankAccount:
    # Class attribute
    branch_name = "KKU Complex"
    branch_number = 1724
    last_loan_number = 0
    last_saving_number = 0

    # Private class attributes
    # account types
    __type_saving = 1
    __type_loan = 2

    # Constructor
    def __init__(self, name, type = None, balance = 0):
        self.name = name
        if type is None:
            self.type = BankAccount.__type_saving
        else:
            self.type = type
        if self.type == BankAccount.__type_saving:
            BankAccount.last_saving_number += 1
            self.account_number = f"{BankAccount.branch_number}-{BankAccount.__type_saving}-{BankAccount.last_saving_number}"
        else:
            BankAccount.last_loan_number += 1
            self.account_number = f"{BankAccount.branch_number}-{BankAccount.__type_loan}-{BankAccount.last_loan_number}"
        if balance is None:
            self.balance = 0
        else:
            self.balance = balance
    
    # Instance methods
    def print_customer(self):
        print(f"----- Customer Record -----")
        print(f"Name: {self.name}")
        print(f"Account number: {self.account_number}")
        print(f"Account type: {self.type}")
        print(f"Balance: {self.balance}")
        print(f"----- End Record -----")
    
    def deposit(self, amount=0):
        self.balance += amount
        return self.balance
    
    def pay_loan(self, amount=0):
        self.balance += amount
        return self.balance
    



John = BankAccount("John", "saving", 500)
John.deposit(3000)
John.print_customer()
Tim = BankAccount("Tim", "loan", -1000000)
Tim.pay_loan(500000/2)
Tim.print_customer()
Sarah = BankAccount("Sarah", "saving")
Sarah.deposit(50000000)
Sarah.print_customer()
sarahloan = BankAccount("Sarah", "loan", -100000000)
sarahloan.print_customer()