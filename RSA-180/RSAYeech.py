#!/usr/bin/python

k = 40634905927881125837687153L #int("0x219cc6aa0ec13d041c4971",16);
totient = 40634905927850661848135028L;
c = 13016925875285007045101206L;

# Assume ethan was right, in that cipher is indeed e, that makes k the mod
# So d is the modular inverse of c over k

def gcd(a,b): # Euclidean Algorithm
	while a:
		a, b = b%a, a;
	return b;

def egcd(a,b): # Extended Euclidean Algorithm
	if a == 0:
		return (b,0,1);
	else:
		g,y,x = egcd(b%a,a);
		return (g, x - (b // a) * y, y);

def modinv(a,m): # Modular Inverse Finder
	g, x, y = egcd(a,m);
	if g != 1:
		raise Exception('modular inverse does not exist');
	else:
		return x % m;

#d = modinv(c,totient); # Doesn't make sense b/c c is not coprime to totient
#d = modinv(c/2,totient); # Makes 0 sense

f = open("RSASolve.txt","a");

for e in range(0,100000):
	if gcd(e,totient) == 1:
		d = modinv(e,totient);
		m = pow(c,d,k);
		hexM = hex(m);
		#print "e: %d" %(e);
		#print "d: %d" %(d);
		#print "Hex: %s" %(hex(d));
		if len(str(hexM)[2:-1]) % 2 == 0:
			f.write("\n" + str(e) + ": " + str(hexM)[2:-1].decode("hex"));
		#print "Result: %s" %(hex(d)[2:].decode("hex"));


#Str = hexD[2:]
#print Str.decode("hex");
