import json

with open('data/consonants.json') as json_file:
    consonantDict = json.load(json_file)

with open('data/vowels.json') as json_file:
    vowelDict = json.load(json_file)

with open('data/matras.json') as json_file:
    matraDict = json.load(json_file)

class Consonant:
    def __init__(self, char, half=False):
        self.char = char
        self.half = half

    def toggle(self):
        if self.half:
            self.half = False
        else:
            self.half = True

    def getChar(self):
        return self.char

    def __str__(self):
        if(self.half):
            return consonantDict[self.char] + "\u094d"
        return consonantDict[self.char]

class Vowel:
    def __init__(self, char, matra=True):
        self.char = char
        self.matra = matra

    def toggle(self):
        if self.matra:
            self.matra = False
        else:
            self.matra = True

    def getChar(self):
        return self.char

    def __str__(self):
        if(self.matra):
            return matraDict[self.char]
        return vowelDict[self.char]

if __name__=="__main__":
    c = Consonant("k")
    print("Consonant", c.getChar(), "without half", c)
    c.toggle()
    print("Consonant", c.getChar(), "without half", c)
    v = Vowel("a")
    print("Vowel", v.getChar(), "as matra", v)
    v.toggle()
    print("Vowel", v.getChar(), "as vowel", v)
