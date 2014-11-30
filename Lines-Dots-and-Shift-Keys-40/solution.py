#!/usr/bin/python

message = "snhj btwp! ymnx hnumjw xmtzqi gj kfrnqnfw yt dtz, tw rfdgj sty. fsdbfd, fx f wjbfwi, mfaj ymnx kqfl. q1s3x_fsi_i0yx_y0_b0wie"

for i in range(26):
	out = ""
	for a in range(len(message)):
		if ord(message[a]) > 96 and ord(message[a]) < 123:
			out = out + chr((((ord(message[a]) + i) - 97) % 26) + 97)
		else:
			out = out + message[a];
	print "rot-%d: %s\n" %(i,out)
	out = ""
