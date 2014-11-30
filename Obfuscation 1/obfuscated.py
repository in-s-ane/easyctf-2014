#! /usr/bin/python

# The output of this program is: NICEJOBFIGURINGOUTWHATTHISPROGRAMDOESTHEFLAGISVINEGARISTHEBESTCIPHER

text = "SWQHRGZZUSSWWBJWMRQTMRYVWVXJMADMKICSVBZCZXMENGJLVWEUDUQYVSEMKRWUBFJF"
apple = "FOODISYUMMY"

""" OLD CODE:
from itertools import starmap, cycle

def mystery(a, b):
    a = filter(lambda _: _.isalpha(), a.upper())
    #important
    def enc(c,k): return chr(((ord(k) + ord(c)) % 26) + ord('A'))

    return "".join(starmap(enc, zip(a, cycle(b))))

final = mystery(text, apple)
 
print (text)
print (final)
"""

# Decided to just unobfuscate the original code ^_^
def mymystery(text, key):
    filtered = []
    for char in text:
        if char.isalpha():
            filtered.append(char.upper())

    def enc(char, key):
        new = (ord(key) + ord(char)) % 26
        return chr(new + ord('A'))

    charlist = []
    cyclerIndex = 0
    for char in text:
        if cyclerIndex >= len(key):
            cyclerIndex = 0
        charlist.append(enc(char, key[cyclerIndex]))
        cyclerIndex += 1

    return "".join(charlist)

encrypted = mymystery(text, apple)

print "Original Text: " + text
#print "Encryption Test: " + encrypted

def mymysterydecode(text, key):
    filtered = []
    for char in text:
        if char.isalpha():
            filtered.append(char.upper())

    def dec(char, key):
        new = ord(char) - ord('A')
        if (new < ord(key) % 26):
            new += 26
        new -= ord(key) % 26
        while (new < ord('A')):
            new += 26
        return chr(new)

    charlist = []
    cyclerIndex = 0
    for char in text:
        if cyclerIndex >= len(key):
            cyclerIndex = 0
        charlist.append(dec(char, key[cyclerIndex]))
        cyclerIndex += 1

    return "".join(charlist)

decoded = mymysterydecode(text, apple)

print "Decoded Text: " + decoded
