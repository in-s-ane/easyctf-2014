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
		print(tuna.decrypt(cipher).decode())
	except:
		#print("Key :" + key + " failed")
		pass; # save your eye some trouble

def brute():
	alphabet = "a b c d e f g h j k l m n o p q r s t u v w x y z "
	alphabet += alphabet.upper() + "1 2 3 4 5 6 7 8 9 0"
	print("Alphabet loaded: " + alphabet)
	L = alphabet.split()
	L.append(" ")
	tmp = ""
	for i in (2,3,4):
		print i;
		for subset in combinations(L , 2):
			for subsubset in permutations(subset):
				tmp = "".join(subsubset)
				testVal = tmp * (8/i)
				if i == 3:
					testVal = testVal+tmp
				while len(testVal) <= 32:
					whale(testVal , "5ktxaA0e8yaL5tvrXjfKjM4ZYGmgVtSvsS7yZoH9udI=")
					testVal = testVal + tmp

brute()
#osu = "osu"
#key = "osu";
#while len(key) <= 32:
#	whale(key,"5ktxaA0e8yaL5tvrXjfKjM4ZYGmgVtSvsS7yZoH9udI=")
#	key = key + osu;
