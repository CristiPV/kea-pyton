class Car:
    def __init__( self, make, model, bhp, mph ):
        self.make = make
        self.model = model
        self.bhp = bhp
        self.mph = mph
    
    @property
    def make( self ):
        return self.__make

    @property
    def model( self ):
        return self.__model

    @property
    def bhp( self ):
        return self__bhp
    
    @property
    def mph( self ):
        return self__mph

    @make.setter
    def make( self, make ):
        self.__make = make
    
    @model.setter
    def model( self, model ):
        self.__model = model
    
    @bhp.setter
    def bhp( self, bhp ):
        if bhp < 0:
            self.___bhp = 0
        elif bhp > 1479:
            self.__bhp = 1479
        else:
            self.__bhp = bhp
    
    @mph.setter
    def mph( self, mph ):
        if  mph < 0:
            self.__mph = 0
        elif mph > 400:
            self.__mph = 400
        else:
            self.__mph = mph

    def __str__( self ):
        return f'{self.__dict__}'
    
    def __repr__( self ):
        return f'{self.__dict__}'

c1 = Car( "Alfa Romeo", "4C", 1000, 500 )
c2 = Car( "Audi", "A4", 900, -11 )
c3 = Car( "Audi", "TT", -199, 344 )
c4 = Car( "BMW", "2 Series", 1500, 255 )

print( c1 )
print( c2 )
print( c3 )
print( c4 )