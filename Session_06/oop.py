class Person:
    type = 'Mammal'

    def __init__( self, name ):
        self.name = name

class Instructor:
    def __init__( self, course ):
        self.course = course

class Student( Person, Instructor ):
    def __init__( self, name, course, age ):
        Person.__init__( self, name )
        Instructor.__init__( self, course )
        self.age = age

class SubPerson( Person, Instructor ):
    def __init__( self, name, age ):
        super().__init__( name )
        self.age = age

    def name_age( self ):
        return self.name +  str( self.age )

class Animal:
    name = 'Cheddar'

class Example:
    def __init__( self, *args ):
        
        if len( args ) == 1:
            self.name = args[0]

        elif len( args ) == 2:
            self.name = args[0]
            self.age = args[1]

        else:
            raise NotImplementedError

        # self.arguments = args 

class Example2:
    def __init__( self, name=None, age=None ):

        if name != None:
            self.name = name
        
        if age != None:
            self.age = age

p = Person( 'Cristi' )

print( p.__dict__ )

p.surname = 'Purcea'
p.age = '20'

print( p.__dict__ )

# Apparently, if I change a class variable from the instance, it becomes a instance variable :/
p.type = 'wow'

Person.type = 'what ?'

print( p.type )
print( p.__dict__ )

dog = Animal()
cat = Animal()

print( dog.name )
print( cat.name )

Animal.name = 'Loki'

print( dog.name )
print( cat.name )

print( Person.__dict__ )

e = Example( 'Loki' )

# print( e.arguments )
print( e.__dict__ )

e2 = Example2( None, 12 )
print( e2.__dict__ )

s = SubPerson( 'Hello there', 12 )
print( s.__dict__ )
print( s.__class__.__dict__ )
print( s.type )
print( s.name_age() )

stud = Student( 'Claus', 'CS', 35 )
print( stud.__dict__ )
print( stud.type )
