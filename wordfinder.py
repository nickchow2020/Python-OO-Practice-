"""Word Finder: finds random words from a dictionary."""
from random import choice

class WordFinder:
    """
        Randomly return a words that is from the file   

        >>> my_new = WordFinder("testing.txt")
        There total of 5 words

        >>> my_new.random() in ["hello","word","how","are","you"]
        True

        >>> my_new.random() in ["hello","word","how","are","you"]
        True

        >>> my_new.random() in ["hello","word","how","are","you"]
        True

    """

    def __init__(self,filepath):
        self.filepath = filepath
        self.words = open(self.filepath,"r")
        self.total = self.printWords()
        print(f"There total of {len(self.total)} words")
    

    def printWords(self):
        return [ wd.strip() for wd in self.words]


    def random(self):   
        return choice(self.total)

class SpecialWordFinder(WordFinder):

    def printWords(self):
        return [wd.strip() for wd in self.words if wd.strip() and not wd.startswith("#")]

