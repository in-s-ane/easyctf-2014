def hash1(n):
    ret = [0]*16
    for i in range(len(n)):
        ret[i%16] += ord(n[i])
    return "".join([chr(i%26 + 97) for i in ret])

def unhash():
    a = ""
    for c in "dqcxxkgegmrunaue":
        a += chr(ord(c) - 97 + (26 * 3))
        # To reverse the modulus operation, we can just add a multiple of 26
        # that will give us a result in the ascii alphabetical range
    print a

unhash()
