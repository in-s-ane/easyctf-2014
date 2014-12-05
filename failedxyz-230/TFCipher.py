import string
from twofish import Twofish
from itertools import permutations
from itertools import combinations

def whale(key , cipher):
	#Define key:
	#key = str(raw_input("Key:	"))
	#cipher = str(raw_input("Cipher:	   "))

	#Get key:

	try:
		tuna = Twofish(key)
		print(key + ": " + tuna.decrypt(cipher).decode())
	except:
		#print("Key :" + key + " failed")
		pass; # save your eye some trouble
		#print "Nope"

def brute():
	alphabet = string.printable

	print("Alphabet loaded: " + alphabet)
        L = [l for l in alphabet]
	L.append(" ")
	tmp = ""
	for i in (16,24,32):
		print i;
		for subset in combinations(L , i):
			for subsubset in permutations(subset):
				tmp = "".join(subsubset)
				whale(tmp , "5ktxaA0e8yaL5tvrXjfKjM4ZYGmgVtSvsS7yZoH9udI=")

brute()
#osu = "osu"
#key = "osu";
#while len(key) <= 32:
#	whale(key,"5ktxaA0e8yaL5tvrXjfKjM4ZYGmgVtSvsS7yZoH9udI=")
#	key = key + osu;
