class Bank:
    def __init__( self ):
        self.accounts = []

    def add_accounts( self, accounts ):
        for account in accounts:
            account_owners = [ _account.cust.name for _account in self.accounts ]
            if account.cust.name not in account_owners: 
                self.accounts.append( account )

    @property
    def accounts( self ):
        return self.__accounts
    
    @accounts.setter
    def accounts( self, accounts ):
        self.__accounts = accounts

    def __str__( self ):
        return f'{self.__dict__}'

    def __repr__( self ):
        return f'{self.__dict__}'

class Account:
    def __init__ (self, no, cust ):
        self.no = no
        self.cust = cust

    @property
    def no( self ):
        return self.__no
    
    @property
    def cust( self ):
        return self.__cust 

    @no.setter
    def no( self, no ):
        self.__no = no
    
    @cust.setter
    def cust( self, cust ):
        self.__cust = cust

    def __str__( self ):
        return f'{self.__dict__}'

    def __repr__( self ):
        return f'{self.__dict__}'

class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name( self ):
        return self.__name

    @property
    def age( self ):
        return self.__age
    
    @name.setter
    def name( self, name ):
        self.__name = name

    @age.setter
    def age( self, age ):
        if ( age < 18 ):
            self._age = 18
        else:
            self.__age = age

    def __str__( self ):
        return f'{self.__dict__}'

    def __repr__( self ):
        return f'{self.__dict__}'



c1 = Customer( "Cristi", 15 )
a1 = Account( 1, c1 )
a2 = Account( 2, c1 )
bank = Bank()
bank.add_accounts( [a1, a2] )
print( bank.accounts )
print( bank )