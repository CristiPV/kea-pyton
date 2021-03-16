class Machine:
    def __init__( self, powered_on ):
        self.powered_on = powered_on
    
    def power_switch( self ):
        self.powered_on = not self.powered_on

    @property
    def powered_on( self ):
        return self.__powered_on
    
    @powered_on.setter
    def powered_on( self, powered_on ):
        self.__powered_on = powered_on

class Printer( Machine ):
    def __init__( self, powered_on, text="" ):
        super().__init__( powered_on )
        self.papertray = Papertray( text )

    def print( self ):
        if self.powered_on:
            print( self.papertray.current_paper )
        else:
            print( "The device is turned off." )

    @property
    def papertray( self ):
        return self.__papertray
    
    @papertray.setter
    def papertray( self, papertray ):
        self.__papertray = papertray

class Papertray():
    def __init__( self, text="" ):
        self.paper_list = [ text ]
        self.current_paper = self.paper_list[0]

    def load_paper( self, text="" ):
        self.current_paper = text
        self.paper_list.append( self.current_paper )
    
    def use_paper( self, pos=0 ):
        self.current_paper = self.paper_list[pos % len(self.paper_list)]
    
    @property
    def paper_list( self ):
        return self.__paper_list
    
    @property
    def current_paper( self ):
        return self.__current_paper
    
    @paper_list.setter
    def paper_list( self, paper_list ):
        self.__paper_list = paper_list
    
    @current_paper.setter
    def current_paper( self, current_paper ):
        self.__current_paper = current_paper

    
printer = Printer( False, "Hello World" )
printer.print()
printer.power_switch()
printer.print()
printer.papertray.load_paper( "I just loaded a new paper" )
printer.print()
printer.papertray.use_paper( 2 )
printer.print()