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
	alphabet = string.printable[0:62] # failedxyz said it's alphanumeric

	print("Alphabet loaded: " + alphabet)
        L = [l for l in alphabet]
	L.append(" ")
	tmp = ""
	counter = 0;
	for i in (16,24,32):
		print i;
		for subset in combinations(L , i):
			for subsubset in permutations(subset):
				if counter % 1000000 == 0:
					print counter
				tmp = "".join(subsubset)
				whale(tmp , "5ktxaA0e8yaL5tvrXjfKjM4ZYGmgVtSvsS7yZoH9udI=")
				counter+=1

#brute()
#osu = "osu"
#key = "osu";
#while len(key) <= 32:
#whale("L"*32,"5ktxaA0e8yaL5tvrXjfKjM4ZYGmgVtSvsS7yZoH9udI=")
#	key = key + osu;
whale("myNameIsMichaelZhang","5ktxaA0e8yaL5tvrXjfKjM4ZYGmgVtSvsS7yZoH9udI");
whale("lostlonelinessliberation","5ktxaA0e8yaL5tvrXjfKjM4ZYGmgVtSvsS7yZoH9udI");
whale("LostLonelinessLiberation","5ktxaA0e8yaL5tvrXjfKjM4ZYGmgVtSvsS7yZoH9udI");
whale("LostLoneLinessLiberation","5ktxaA0e8yaL5tvrXjfKjM4ZYGmgVtSvsS7yZoH9udI");
whale("lostLonelinessLiberation","5ktxaA0e8yaL5tvrXjfKjM4ZYGmgVtSvsS7yZoH9udI");

#whale("")
