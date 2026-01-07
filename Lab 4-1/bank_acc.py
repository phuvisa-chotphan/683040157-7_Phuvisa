from P2 import BankAccount

John = BankAccount("John", 1 , 500)
John.deposit(3000)
John.print_customer()

Tim = BankAccount("Tim", 2 , -1000000)
Tim.pay_loan(500000)
Tim.print_customer()

Sarah = BankAccount("Sarah", 1)
Sarah.deposit(50000000)
Sarah.print_customer()

sarahloan = BankAccount("Sarah", 2, -100000000)
sarahloan.print_customer()