"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self,start):
        """
            Initial class constructor with self and start properties

            attributes: 
            ----------------------------
            self: represent class itself
            start: store initial value and set start property value

        """
        self.init = start
        self.start = start
    
    def __repr__(self):
        return f"<SerialGenerator start={self.init} next={self.start + 1}>"

    def generate(self):
        """
            print start property out and increase one each time the function calls 
        """
        print(self.start)
        self.start += 1
    
    def reset(self):
        """
            reset start property to it's initial value
        """
        self.start = self.init

    