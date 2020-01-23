import json
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

def genToken(inputStr):
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
            return Consonant(key)
        elif key in vowelDict:
            return Vowel(key)
        else:
            index -= 1

def genTokenList(inputStr, maximalMap=4):
    """
    Returns the generated token list after parsing :inputStr:
    """
    index = 0
    tokenList = []
    while(index < len(inputStr)):
        t = genToken(inputStr[index:index+maximalMap])
        tokenList.append(t)
        index = index + len(t.getChar())
    return tokenList

def parse(inputStr):
    """
    Parses the inputStr and returns a unicode string of the
    transliterated string.
    """
    tokenList = vowelToggle(consonantToggle(genTokenList(inputStr)))
    return reduce(lambda x,y: str(x)+str(y), tokenList)

if __name__=="__main__":
    import sys
    args = sys.argv[1:]
    if(len(args) == 1):
        print("The transliteration of", args[0], "is", parse(args[0]))
    else:
        print("Usage: python3 transliterator.py <word>")
