import sys


def decode(encryptedText, knownWord, minlength, maxlength):

    found = False

    newWord = combine(knownWord, minlength, maxlength)

    for line in encryptedText:
        for word in line:
            if word == newWord:
                found = True
                return found

        
def combine(knownWord, minlength, maxlength):

    code =
    newWord = ' '

    for i in knownWord:
        newWord += str(encode(i, code))

    return newWord


def encode(ch, code):

    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "l", "m", "n", "o"
                , "p", "q", "r", "s", "t", "u", "v", "x" "y", "z"]

    for i in alphabet:
        if ch == i:
            return alphabet[((alphabet.index(i) + code) % 22)]


if __name__ == '__main__':
    encryptedText = open(sys.argv[1], 'r')
    knownWord = sys.argv[2]
    minlength = int(sys.argv[3])
    maxlength = int(sys.argv[4])
    decode(encryptedText.readline(), knownWord, minlength, maxlength)
