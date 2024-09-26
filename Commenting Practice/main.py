class BankAccount:
    #This sets the balance that everything will use to your balance and account number.
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    #This deposits money to your account if the money you deposit is more than 0.
    def deposit(self, amount):
        #Checks if you are trying to deposit negative amounts of money.
        if amount > 0:
            self.balance += amount
            return True
        return False
    #This will withdraw money from your account, if you ask to withdraw any amount greater than 0.
    def withdraw(self, amount):
        #Checks if you are trying to withdraw positive amounts of money.
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False
    #Returns your balance to whatever called the function.
    def get_balance(self):
        return self.balance
#This functions allows you to create an account.
def create_account():
    account_number = input("Enter account number: ")
    initial_balance = float(input("Enter initial balance: "))
    return BankAccount(account_number, initial_balance)
    #This is the main part of the code that will allow you input things and call the other functions. Without htis, you would just have functions that sit around doing nothing.
def main():
    accounts = {}
    while True:
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        #Checks if you chose to create an acount.
        if choice == '1':
            account = create_account()
            accounts[account.account_number] = account
            print(f"Account {account.account_number} created successfully!")
        #Checks if you chose to do anything other than creating an account or leaving.
        elif choice in ['2', '3', '4']:
            account_number = input("Enter account number: ")
            #Checks if your account exists, and sets your account to be that one.
            if account_number in accounts:
                account = accounts[account_number]
                #Checks if you chose to deposit money.
                if choice == '2':
                    amount = float(input("Enter deposit amount: "))
                    #Checks if you were able to deposit.
                    if account.deposit(amount):
                        print(f"Deposited ${amount:.2f} successfully!")
                    #Tells you you did it wrong if it can't deposit the money.
                    else:
                        print("Invalid deposit amount.")
                #Checks if you chose to withdraw money.
                elif choice == '3':
                    amount = float(input("Enter withdrawal amount: "))
                    #Checks if you successfully withdrew the money you wanted to.
                    if account.withdraw(amount):
                        print(f"Withdrawn ${amount:.2f} successfully!")
                    #Tells you that you did it wrong.
                    else:
                        print("Invalid withdrawal amount or insufficient funds.")
                #Tells you how much money you have if you entered a 4.
                else:
                    print(f"Current balance: ${account.get_balance():.2f}")
            #Tells you they couldn't find your account after you enter an account number.
            else:
                print("Account not found.")

        #Checks if you wanted to leave, and leaves if you did.
        elif choice == '5':
            print("Thank you for using our banking system. Goodbye!")
            break
        #Tells you to try again if you entered an invalid number.
        else:
            print("Invalid choice. Please try again.")
#Starts the function main which starts everything up.
if __name__ == "__main__":
    main()