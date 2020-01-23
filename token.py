import json

# Load mapping dicts
with open('data/consonants.json') as json_file:
    consonantDict = json.load(json_file)

with open('data/vowels.json') as json_file:
    vowelDict = json.load(json_file)

with open('data/matras.json') as json_file:
    matraDict = json.load(json_file)

class EHConsonant:
    """
    Represents a consonant token
    :attr: char - English representation of the token
    :attr: half (False) - Flag to print the token as a half consonant
    """
    def __init__(self, char, half=False):
        self.char = char
        self.half = half

    def toggle(self):
        """
        Toggle the flag half
        """
        if self.half:
            self.half = False
        else:
            self.half = True

    def getChar(self):
        """
        Return char
        """
        return self.char

    def __str__(self):
        if(self.half):
            return consonantDict[self.char] + "\u094d"
        return consonantDict[self.char]

class EHVowel:
    """
    Represents a vowel token
    :attr: char - English representation of the token
    :attr: matra (True) - Flag to print the token as a matra
    """
    def __init__(self, char, matra=True):
        self.char = char
        self.matra = matra

    def toggle(self):
        """
        Toggle the flag matra
        """
        if self.matra:
            self.matra = False
        else:
            self.matra = True

    def getChar(self):
        """
        Return char
        """
        return self.char

    def __str__(self):
        if(self.matra):
            return matraDict[self.char]
        return vowelDict[self.char]
class HRConsonant:
    """
    Represents a consonant token
    :attr: char - Roman representation of the token
    :attr: half (False) - Flag to print the token as a half consonant
    """
    def __init__(self, char, half=False):
        self.char = char
        self.half = half

    def toggle(self):
        """
        Toggle the flag half
        """
        if self.half:
            self.half = False
        else:
            self.half = True

    def getChar(self):
        """
        Return char
        """
        return self.char

    def __str__(self):
        if(self.half):
            return consonantDict[self.char] 
        return consonantDict[self.char]+ "\u0061"

class HRVowel:
    """
    Represents a vowel token
    :attr: char - Roman representation of the token
    """
    def __init__(self, char):
        self.char = char

    def getChar(self):
        """
        Return char
        """
        return self.char

    def __str__(self):

        return vowelDict[self.char]


if __name__=="__main__":
    c = EHConsonant("k")
    print("Consonant", c.getChar(), "without half", c)
    c.toggle()
    print("Consonant", c.getChar(), "without half", c)
    v = EHVowel("a")
    print("Vowel", v.getChar(), "as matra", v)
    v.toggle()
    print("Vowel", v.getChar(), "as vowel", v)
