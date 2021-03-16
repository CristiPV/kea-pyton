class P:
   def __init__( self, name, alias ):
      self.name = name       # public
      self.__alias = alias   # private

   def who(self):
      print('name  : ', self.name)
      print('alias : ', self.__alias)

class X:
    def __init__( self, x ):
        self.set_x( x )

    def get_x( self ):
        return self.__x

    def set_x( self, x ):
        if x > 1000:
            self.__x = 1000
        elif x < 0:
            self.__x = 0
        else:
            self.__x = x

class Y:
    def __init__( self, x ):
        self.x = x # self.x is now the @x.setter

    @property
    def x( self ):
        return self.__x # this is a private variable

    @x.setter
    def x( self, x ):
        if x > 1000:
            self.__x = 1000
        elif x < 0:
            self.__x = 0
        else:
            self.__x = x

class S:
    def __init__( self, name ):
        self.name = name
    def __repr__( self ):
        return f'{self.__dict__}'
    def __str__( self ):
        return f'Name: {self.name}'
    def __add__( self, other ):
        return S(f'{self.name} {other.name}')

class Deck:
    def __init__( self, cards ):
        self.cards = list( cards )
    def __getitem__( self, key ):
        return self.cards[key]
    def __repr__( self ):
        return f'{self.__dict__}'

p = P('Claus', 'clbo')
p.who()
print( p.__dict__ )
print( p._P__alias )
p._P__alias = 'wow'
print ( p._P__alias )

x1 = X( 3 )
x2 = X( 50 )
x1.set_x( x1.get_x() + x2.get_x() )
print ( x1.get_x() )

y1 = Y( 10 )
y2 = Y( 15 )
print( y1.__dict__ )
print ( y1.x )
y1.x = y1.x + y2.x
print ( y1.x )
y1._Y__x = -10
print( y1.x )

s1 = S( "Cristian" )
s2 = S( "Valentin" )
s3 = s1.__add__( s2 )
print( s3 )

d1 = Deck( ["K", "A", 2, 3] )
print( d1 )
print ( d1[0] )