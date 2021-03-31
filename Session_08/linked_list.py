class Node:
    def __init__( self, data ):
        self.data = data
        self.next = None

    def __str__( self ):
        return f"Data: { self.data }"
    
    def __repr__( self ):
        return f"{ self.__dict__ }"

class LinkedList:
    def __init__( self ):
        self.head = None
    
    def __add__( self, other ):
        new_list = LinkedList()

        current = self.head
        if current == None:
            return other
        else:
            new_list.append( current.data )
            new_current = new_list.head

            while current.next != None:
                current = current.next
                new_list.append( current.data )
                new_current = new_current.next
                
            new_current.next = other.head

        return new_list    
    
    def __mul__( self, amount ):
        new_list = self.copy()

        for i in range( amount - 1 ):
            new_list += new_list

        return new_list

    def __contains__( self, item ):
        if self.head == None:
            return False
        else:
            current = self.head
            while current.next != None:
                if current.data == item:
                    return True
                current = current.next
            if current.data == item:
                return True
            return False

    def __getitem__( self, index ):
        current = self.head
        i = 0
        if index < 0:
            index += len( self )
        while i < index:
            i += 1
            current = current.next
        return current

    def __setitem__( self, index, item ):
        self[index].data = item.data

    def __delitem__( self, index ):
        if self[index] == self.head:
            self.head = self.head.next
        elif self[index] == self[ len( self ) - 1 ]:
            print( self[index - 1] )
            self[ index - 1 ].next = None
        else:
            self[ index - 1 ].next = self[ index + 1 ]

    def __len__( self ):
        if self.head == None:
            return 0
        else:
            current = self.head
            length = 1
            while current.next != None:
                current = current.next
                length += 1
            return length

    def __str__( self ):
        current = self.head
        string = "Nodes: [ "

        if self.head == None:
            string += "]"
        else:
            while current.next != None:
                string += f"{ current.data }, "
                current = current.next
            string += f"{ current.data } ]"

        return string
    
    def __repr__( self ):
        return f"{ self.__dict__ }"

    def append( self, item ):
        current = self.head
        if current == None:
            self.head = Node( item )
        else:
            while current.next != None:
                current = current.next
            current.next = Node( item )
    
    def pop( self, position = -1 ):
        current = self[ position - 1 ]
        if current.next.next != None:
            current.next = current.next.next
        else:
            current.next = None

    def insert( self, position, item ):
        new_node = Node( item )
        new_node.next = self[position]
        self[ position - 1 ].next = new_node

    def remove( self, item ):
        self.pop( self.index( item ) )

    def copy( self ):
        new_list = LinkedList()
        new_list.head = self.head
        return new_list

    def count( self, item ):
        counter = 0
        current = self.head
        if current == None:
            return counter
        else:
            while current.next != None:
                if current.data == item:
                    counter += 1
                current = current.next
            if current.data == item:
                counter += 1
            return counter

    def index( self, item ):
        if self.head == None:
            return -1
        else:
            index = 0
            current = self.head

            if current.data == item:
                return index
            while current.next != None:
                current = current.next
                index += 1
                if current.data == item:
                    return index
            
            return -1

    def reverse( self ):
        for i in range( int( len( self ) / 2 ) ):
            x = self[ len( self ) - i - 1 ].data
            self[ len( self ) - i - 1 ].data = self[i].data
            self[i].data = x

    def clear( self ): 
        self.head = None

list1 = LinkedList()



