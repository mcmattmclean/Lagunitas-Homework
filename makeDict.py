import sys
import string
from collections import Counter

# Change passed word to lower case and remove any attached punctuation
def removePunctuation(word):
    return word.lower().translate(str.maketrans('', '', string.punctuation))

# Attempt to open the passed file name and return a Counter object with each word in the file counted
def makeDict(filename):
    with open (filename, "r") as myfile:
        myDict = Counter()
        for line in myfile:
            for word in line.split():
                myDict[removePunctuation(word)]+=1
        return myDict

if __name__ == "__main__":
     print(makeDict(sys.argv[1]))
