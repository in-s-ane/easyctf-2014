# This question was initially extremely vague as to the format of the answer, but it was soon clarified
'''
args[0] is a result of XOR encryption on two hexadecimal strings. You only know one of the two original strings, args[1], can you find the other?
Clarification: after finding the second string you should print the ascii representation of it as the answer in the Python Editor.
'''

a = hex(int(args[0], 16) ^ int(args[1], 16))[2:][:-1]
b = ""
i = 0
while i < len(a) - 1:
  b += chr(int(a[i] + a[i+1], 16))
  i += 2

print b
