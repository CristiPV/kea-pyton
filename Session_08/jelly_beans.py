class JellyBean:
    def __init__( self, mass = 0 ):
        self.mass = mass

    def __add__( self, other ):
        other_mass = other.mass
        other.mass = 0
        return JellyBean( self.mass + other_mass )

    def __sub__( self, other ):
        self_mass = self.mass
        self.mass -= other.mass

    def __str__( self ):
        return f"Mass: { self.mass }"
    
    def __repr__( self ):
        return f"{ self.__dict__ }"

jelly = JellyBean( 3 )
bean = JellyBean( 2 )

jelly += bean

print( jelly )
print( bean )