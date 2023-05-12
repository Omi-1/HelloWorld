class Bank_account:

    def __init__(self, acct_no, acct_name, acct_bal):
        self.acct_no = acct_no
        self.acct_name = acct_name
        self.acct_bal = acct_bal
        print(f"Your accont balance is {self.acct_bal}")
        print(f"Your accont number is {self.acct_no}")
        print(f"Your accont name is {self.acct_name}")
    def deposit(self, amt):
        acct_bal= self.acct_bal+amt
        print(f"Deposit sucessful,new balance is {acct_bal}")

    def withdraw(self, amt):
        if self.acct_bal >= amt:
            print(f"Withdrawal successful")
        else:
            self.acct_bal < amt
            print(f"Withdrawal declined")


value =Bank_account(3895094,"Nunsi",3400)
value.deposit(98)
value.withdraw(3498)
