class Deck:
    def __init__( self ):
        self.cards = ['A', 2, 3, 4, 5, 6, 7, 9, 10, 'J', 'Q', 'K']

    def __getitem__( self, key ):
        return self.cards[key]

    def __setitem__( self, key, item ):
        self.cards[key] = item

    def __delitem__( self, key ):
        del self.cards[key]

    def __repr__( self ):
        return f'{self.__dict__}'

    def __str__( self ):
        return f'Cards: {self.cards}'

    def __len__( self ):
        return len( self.cards )

    def __add__( self, item ):
        if type( item ) == type( self ):
            return self.cards + item.cards
        else:
            return self.cards + item
    
# Init
deck = Deck()

# Get Item
print( deck[-1] )
print( deck[1:4] )

# Repr
print( deck )

# Len
print( len( deck ) )

# Add
deck_to_add = Deck()
print( type( deck_to_add ) )
print( deck + deck_to_add )
print( deck + [9, 12] )

# Set
value = 'Added'
deck[4] = value
print( str( deck ) )

# Del
del deck[4]
print( str( deck ) )