import json
from token import EHConsonant, EHVowel,HRConsonant,HRVowel
from functools import reduce

class EHParser:
    def __init__(self, maximalMap=3):
        self.maximalMap = maximalMap

    def vowelToggle(self, tokenList):
        """
        Modifies the vowels in :tokenList: to print as a vowel
        iff the previous token is also a vowel. All other vowels
        are printed as matras.
        """
        for i in range(len(tokenList)):
            if (i == 0 and isinstance(tokenList[i], EHVowel)) or \
               (i != 0 and isinstance(tokenList[i], EHVowel) and \
                isinstance(tokenList[i - 1], EHVowel)):
                tokenList[i].toggle()

        return tokenList

    def consonantToggle(self, tokenList):
        """
        Modifies the consonants in :tokenList: to print as a half character
        iff the next token is also a consonant. All other consonants
        are printed as full characters.
        """
        for i in range(len(tokenList)):
            if (i == len(tokenList) - 1 and isinstance(tokenList[i], EHConsonant)) or \
               (i != len(tokenList) - 1 and isinstance(tokenList[i], EHConsonant) and \
                isinstance(tokenList[i + 1], EHConsonant)):
                tokenList[i].toggle()

        return tokenList

    def genToken(self, inputStr):
        """
        Generate maximal character from mapping jsons
        """
        # Load mapping dicts
        with open('data/consonants.json') as json_file:
            consonantDict = json.load(json_file)

        with open('data/vowels.json') as json_file:
            vowelDict = json.load(json_file)

        index = len(inputStr)
        while(index > 0):
            key = inputStr[:index]
            if key in consonantDict:
                return EHConsonant(key)
            elif key in vowelDict:
                return EHVowel(key)
            else:
                index -= 1

    def genTokenList(self, inputStr):
        """
        Returns the generated token list after parsing :inputStr:
        """
        index = 0
        tokenList = []
        while(index < len(inputStr)):
            t = self.genToken(inputStr[index:index+self.maximalMap])
            tokenList.append(t)
            index = index + len(t.getChar())
        return tokenList

    def parse(self, inputStr):
        """
        Parses the inputStr and returns a unicode string of the
        transliterated string.
        """
        tokenList = self.vowelToggle(self.consonantToggle(self.genTokenList(inputStr)))
        return reduce(lambda x,y: str(x)+str(y), tokenList)

class HRParser:
    def __init__(self, maximalMap=1):
        self.maximalMap = maximalMap

    def consonantToggle(self, tokenList):
        """
        Modifies the consonants in :tokenList: to print as a half character
        iff the next token is also a consonant. All other consonants
        are printed as full characters.
        """
        for i in range(len(tokenList)):
            if ((i != len(tokenList) - 1 and isinstance(tokenList[i], HRConsonant) and isinstance(tokenList[i+1], HRConsonant)) or \
                (i == len(tokenList) - 1 and isinstance(tokenList[i], HRConsonant))):
                tokenList[i].toggle()

        return tokenList

    def genToken(self, inputStr):
        """
        Generate maximal character from mapping jsons
        """
        # Load mapping dicts
        with open('data/romanconsonants.json') as json_file:
            HRconsonantDict = json.load(json_file)

        with open('data/romanvowels.json') as json_file:
            HRvowelDict = json.load(json_file)

        with open('data/romanmatras.json') as json_file:
            HRmatraDict = json.load(json_file)

        index = len(inputStr)
        while(index > 0):
            key = inputStr[:index]
            if key in HRconsonantDict:
                return HRConsonant(key)
            elif key in HRvowelDict:
                return HRVowel(key)
            elif key in HRmatraDict:
                return HRVowel(key)
            else:
                index -= 1

    def genTokenList(self, inputStr):
        """
        Returns the generated token list after parsing :inputStr:
        """
        index = 0
        tokenList = []
        while(index < len(inputStr)):
            t = self.genToken(inputStr[index:index+self.maximalMap])
            tokenList.append(t)
            index = index + len(t.getChar())
        return tokenList

    def parse(self, inputStr):
        """
        Parses the inputStr and returns a unicode string of the
        transliterated string.
        """
        tokenList = self.consonantToggle(self.genTokenList(inputStr))
        return reduce(lambda x,y: str(x)+str(y), tokenList)

if __name__=="__main__":
    import sys
    args = sys.argv[1:]
    if(len(args) == 2):
        if(args[0] == "Hindi"):
            parser = EHParser()
            print("The transliteration of", args[1], "is", parser.parse(args[1]))
        elif(args[0] == "Roman"):
            parser = HRParser()
            print("The transliteration of", args[1], "is", parser.parse(args[1]))
        else:
            print("Usage: python3 transliterator.py <Roman|Hindi> <word>")
    else:
        print("Usage: python3 transliterator.py <Roman|Hindi> <word>")
