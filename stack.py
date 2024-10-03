class Stack:
    """ Creates a LIFO structure using a list. """
    # Python doesn't have a native class called Stack,
    # so this module shouldn't have any problems.
    
    def __init__(self):
        """ Initialize a stack as an empty list. """
        self.stack = []
        
    def isEmpty(self):
        """_summary_

        Returns:
            Boolean: Returns True if the stack is empty. False otherwise.
        """
        return self.stack == []
    
    def push(self, item):
        """
        Add an item to the stack.

        Args:
            item (any): This can be of any data type, 
                        such as an integer, string, or a custom object.
        
        """
        self.stack.append(item)
    
    def pop(self):
        """
        Remove and return the last item added to the stack.

        Returns:
            any: The item that was removed from the stack. 
                If the stack is empty, nothing is returned.
        """
        if not self.isEmpty(self):
            return self.stack.pop()
    
    def peek(self):
        """
        Return the top element of the stack.

        Returns:
            any: The item added last to the stack.
                If the stack is empty, nothing is returned.
        """
        if not self.isEmpty():
            return self.stack[-1]
        
    def size(self):
        """
        Returns the number of items in the stack.

        Returns:
            int: The total number of items currently in the stack.
        """
        return len(self.stack)