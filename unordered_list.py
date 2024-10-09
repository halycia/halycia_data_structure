from node import Node

class Unordered_List:
    """ Creates an unordered list using relative position. """
    # because Python already has a native class called List,
    # I added my name to this module to avoid problems. 
    
    def __init__(self):
        """ Initialize an empty list. """
        self.head = None
    
    def __repr__(self):
        """ Simulates how python """
        current = self.head
        representation = ""
        
        if current is not None:
            representation = "[" + str(current.getData())
            current = current.getNext()
            while current is not None:
                representation += (", " + str(current.getData()))
                current = current.getNext()
            representation += "]"
        else:
            representation = "[]"
        
        return representation

    def isEmpty(self):
        """ Returns True if the list is empty. False otherwise. """
        return self.head is None
    
    def add_item(self,item):
        """ Add item to the front of the list. """
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        
    def append_item(self, item):
        """ Add item to the end of the list. """
        temp = Node(item)
        if self.isEmpty():
            self.head = temp
        else:
            current = self.head
            while current.getNext() is not None:
                current = current.getNext()
            current.setNext(temp)
    
    def insert_item(self, position, item):
        """
        Inserts the item at the specified position.
        Args: (int, any).
        """
        counter = 0
        current = self.head
        
        if position < 0 or position > self.size():
            raise IndexError("Position out of bounds.")
        
        new_item = Node(item)

        if position == 0:
            new_item.setNext(self.head)
            self.head = new_item
        else:
            while counter < position - 1:
                current = current.getNext()
                counter += 1

            new_item.setNext(current.getNext())
            current.setNext(new_item)

        def size(self):
            """ Returns the size of the list. """
            current = self.head
            count = 0
            while current is not None:
                count = count + 1
                current = current.getNext()

            return count

    def search(self,item):
        """ 
        Takes an item as argument.
        Returns True if the item is found in the list. False otherwise. 
        """
        current = self.head
        found = False
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item):
        """ 
        Takes an item as argument. 
        Remove the item from the list if it is found.
        """
        current = self.head
        previous = None
        found = False
        
        while not found and (current is not None):
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if found:
            if previous is None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())

    def getTail(self):
        """ Returns the last item from the list. """
        current = self.head
        while current.getNext() is not None:
            current = current.getNext() 
        return current.getData()
    