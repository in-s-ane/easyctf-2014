import random, socket, time
'''
Since the float comparison used by the server isn't "correct," we need to
enhance the precision of the float that we send to the server. The default
precision that the string conversion of a float gives is too imprecise for the
float comparison to evaluate to true, so we simply format the float to have a
certain precision
'''

while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(("python.easyctf.com", 10663))
        # Python's random.seed() implementation first tries to seed with
        # os.urandom, and if that is not implemented, then it seeds with
        # int(time.time() * 256)
        random.seed(int(time.time() * 256))
        sock.recv(1024)
        random_secret=random.random()
        sock.send("{:.20f}".format(random_secret))
        response = sock.recv(1024)
        if not 'NOPE' in response:
            print response
            break

        sock.close()

