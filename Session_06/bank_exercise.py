class Bank:
    def __init__( self, account_list ):
        self.account_list = account_list

    def add_account( self, account ):
        self.account_list.append( account )

    def print_account_list( self ):
        for account in self.account_list:
            print( 'Customer: ', account.customer.__dict__, '\nBalance: ', account.balance )

class Account:
    def __init__( self, *args ):
        if len( args ) >= 1:
            self.customer = args[0]
        if len( args ) >= 2:
            self.balance = args[1]


class Customer:
    def __init__( self, *args ):
        if len( args ) >= 1:
            self.name = args[0]
        if len( args ) >= 2:   
            self.age = args[1]         
        if len( args ) >= 3:
            self.gender = args[2]

c1 = Customer( 'Claus', 32, 'male' )
c2 = Customer( 'Alex', 27, 'unknown' )
c3 = Customer( 'Cristi', 20 )
c4 = Customer( 'Jan' )

a1 = Account( c1, 200 )
a2 = Account( c2, 300 )
a3 = Account( c3, 300 )

b1 = Bank( [a1, a2] )

b1.add_account( a3 )

b1.print_account_list()
