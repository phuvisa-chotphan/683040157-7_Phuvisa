from bank_acc import BankAccount

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