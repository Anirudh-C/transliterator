from token import Consonant, Vowel
from functools import reduce

def vowelToggle(tokenList):
    """
    Modifies the vowels in :tokenList: to print as a vowel
    iff the previous token is also a vowel. All other vowels
    are printed as matras.
    """
    for i in range(len(tokenList)):
        if (i == 0 and isinstance(tokenList[i], Vowel)) or \
           (i != 0 and isinstance(tokenList[i], Vowel) and isinstance(tokenList[i - 1], Vowel)):
            tokenList[i].toggle()

    return tokenList

def consonantToggle(tokenList):
    """
    Modifies the consonants in :tokenList: to print as a half character
    iff the next token is also a consonant. All other consonants
    are printed as full characters.
    """
    for i in range(len(tokenList)):
        if (i == len(tokenList) - 1 and isinstance(tokenList[i], Consonant)) or \
           (i != len(tokenList) - 1 and isinstance(tokenList[i], Consonant) and \
            isinstance(tokenList[i + 1], Consonant)):
            tokenList[i].toggle()

    return tokenList

def genTokenList(inputStr):
    """
    Returns the generated token list after parsing :inputStr:
    """
    return []

def parse(inputStr):
    """
    Parses the inputStr and returns a unicode string of the
    transliterated string.
    """
    tokenList = vowelToggle(consonantToggle(genTokenList(inputStr)))
    return reduce(lambda x,y: str(x)+str(y), tokenList)

if __name__=="__main__":
    pass
