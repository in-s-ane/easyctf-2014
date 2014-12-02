To break this problem, we have to understand how the key for a rsa is generated.

Since the question only gave you the modulo part of the public key, we need to find both the exponent part of the public key as well as the decryption key.

So here's a brief rundown of how an RSA encryption is generated:

1. We find two primes, p and q, and we generate N, the modulo, which equals to p*q

2. We chose an exponent, which is coprime to the totient function of N

3. The public key is released as (N, e), and the private decryption key d is the multiplicative inverse of e over mod N.

So, we know that N is 0x219cc6aa0ec13d041c4971, which is 40634905927881125837687153 in base 10.

The totient of this is 40634905927850661848135028.

From there, we try every single possible e in existance XD.

Refer to ./RSAYeech.py <max e value> for detail, in there we use the Extended Euclidean Algorithm to find modulo inverse and test for all possible d.

The flag is _probably_ printable, so we perform a check within the program to make our lives easier. So yeah, you hit actual english when e reaches 1197828, which gives you the flag: > rsa_2_easy 
