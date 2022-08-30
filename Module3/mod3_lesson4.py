#Creating a Bank account class
class Bankaccount:
    def __init__(self):
        self.balance = 0
        print("Bank account statement!")

#Deposit 
    def deposit(self):
        amount=float(input("Enter amount to deposit: "))
        self.balance = self.balance + amount
        print('Total deposit:',amount)

#Withdrawal 

    def withdrawal(self):
        amount = float(input("Enter the amount to withdraw: "))
        if self.balance >= amount:
            self.balance = self.balance - amount
            print("Withdraw: ",amount)
        else:
            print("Insuficient Balance")
        
    def account(self):
        print('Available Balance=',self.balance)

#object of class
Feyisayo_Account = Bankaccount()

#Printing the methods with the class
Feyisayo_Account.deposit()
Feyisayo_Account.withdrawal()
Feyisayo_Account.account()