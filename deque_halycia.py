class Deque_halycia:
    """ Creates a double-ended queue structure using a list. """
    # because Python already has a native class called Deque,
    # I added my name to this module to avoid problems. 
    
    def __init__(self):
        """ Initialize a deque as an empty list. """
        self.deque = []
        
    def isEmpty(self):
        """
        Check if the deque is empty.
        Returns true if it is empty. False otherwise.
        """
        return self.deque == []
    
    def addFront(self, item):
        """
        Add an item to the front of the deque. Returns nothing.

        Args:
            item (any): This can be of any data type, 
                        such as an integer, string, or a custom object.
        """
        self.deque.insert(0, item)
    
    def addRear(self, item):
        """
        Add an item to the rear of the deque. Returns nothing.

        Args:
            item (any): This can be of any data type, 
                        such as an integer, string, or a custom object.
        
        """
        self.deque.append(item)
        
    def removeFront(self):
        """
        Remove and return the item from the front of the deque. 
        If the deque is empty, nothing is returned.
        """
        if not self.isEmpty(self):
            return self.deque.pop(0)
    
    def removeRear(self):
        """
        Remove and return the item from the rear of the deque. 
        If the deque is empty, nothing is returned. 
        """
        if not self.isEmpty(self):
            return self.deque.pop()
    
    def peekFront(self):
        """
        Returns the front element of the deque. 
        It doesn't remove it from the deque. 
        If the deque is empty, nothing is returned.
        """
        if not self.isEmpty():
            return self.deque[0]
    
    def peekRear(self):
        """
        Returns the rear element of the deque. 
        It doesn't remove it from the deque. 
        If the deque is empty, nothing is returned.
        """
        if not self.isEmpty():
            return self.deque[-1]
        
    def size(self):
        """
        Returns the number of items in the deque.

        Returns:
            int: The total number of items currently in the deque.
        """
        return len(self.deque)