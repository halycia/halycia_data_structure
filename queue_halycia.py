class Queue_halycia :
    """ Creates a FIFO structure using a list. """
    # because Python already has a native module called Queue,
    # I added my name to this module to avoid problems. 
    
    def __init__(self):
        """ Initialize a queue as an empty list. """
        self.queue = []
        
    def isEmpty(self):
        """
        Check if the queue is empty. 
        
        Returns:
            Boolean: Returns True if the queue is empty. False otherwise.
        """
        if self.queue == []:
            return True
        
    def enqueue(self, item):
        """
        Add an item to the queue.

        Args:
            item (any): This can be of any data type, 
                        such as an integer, string, or a custom object.
        """
        self.queue.append(item)
    
    def dequeue(self):
        """
        Remove and return the front item from the queue.

        Returns:
            any: The item that was removed from the front of the queue. 
                If the queue is empty, nothing is returned.
        """
        if not self.isEmpty():
            return self.queue.pop(0)
            
    def size(self):
        """
        Returns the number of items in the queue.

        Returns:
            int: The total number of items currently in the queue.
        """
        return len(self.queue)