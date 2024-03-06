#Create a class called BankAccount with a constructor that accepts the holder and balance parameters. Start the active attribute as False by default.

class BankAccount:

    def __init__(self, holder='', balance=''):
        self.holder = holder
        self.balance = balance
        self._active = False

    #In the Bank_acount class, add a special method __str__ that returns a message formatted with the account holder and balance. Create two instances of the class and print these instances.

    def __str__(self):
        return f'Account {self.holder} - Balance: ${self.balance}'

account1 = BankAccount('joão', 1000)
account2 = BankAccount('Maria', 500)

print(account1)
print(account2)


# Add a class method called activate_account to the Bank_account class that sets the active attribute to True. Create an instance of the class, call the class method and print the asset value.

    @classmethod
    def active_account(cls, account):
        account._active = True

    account3 = BankAccount('Carlos', 200)




    #Refactor the Bank_account class to use the "pythonic" approach in creating attributes. Use properties if necessary.

    #Create an instance of the class and print the value of the holding property.

    #Create a class called Client_bank with a constructor that accepts 5 attributes. Instantiate 3 objects of this class and assign values ​​to their attributes using the constructor method.

    #Create a class method for the Client_bank_account.
