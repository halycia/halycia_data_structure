from node import Node

class Unordered_List:
    """ Creates an unordered list using relative position. """
    # because Python already has a native class called List,
    # I added my name to this module to avoid problems. 
    
    def __init__(self):
        """ Initialize an empty list. """
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        """ Add item to the front of the list """
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        
    def append(self, item):
        """
        Add item to the end of the list.
        Doen
        """
        temp = Node(item)
        if self.isEmpty():
            self.head == temp
        else:
            current = self.head
            while current.getNext() is not None:
                current.getNext()
            current.setNext(temp)

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        # implement case where the item to be removed isn't found in the list.
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

