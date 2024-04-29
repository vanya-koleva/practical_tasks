class BankAccount:
    def __init__(self, account_number, balance=0):
        """
        Constructor method to initialize the account number and balance.
        """
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        """
        Method to deposit money into the account.
        """
        self.balance += amount

    def withdraw(self, amount):
        """
        Method to withdraw money from the account.
        """
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def get_balance(self):
        """
        Method to retrieve the current balance.
        """
        print(f"Current Account Balance: {self.balance:.2f}")


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0):
        """
        Constructor method to initialize the account number, balance, and interest rate.
        """
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        """
        Method to calculate and add interest to the account balance.
        """
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest


# Testing the functionality of the classes
if __name__ == "__main__":
    bank_account = BankAccount("123456789", 1000)
    bank_account.deposit(500)
    bank_account.withdraw(200)
    bank_account.get_balance()

    savings_account = SavingsAccount("987654321", 2000, 5)
    savings_account.deposit(1000)
    savings_account.calculate_interest()
    savings_account.get_balance()
