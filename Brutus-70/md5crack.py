# A quick and dirty md5 brute force
import hashlib, sys
adjectives = open("adjectives.txt", 'r').read().split('\r\n')
numbers = open("numbers.txt", 'r').read().split('\r\n')
colors = open("colors.txt", 'r').read().split('\r\n')
animals = open("animals.txt", 'r').read().split('\r\n')
num_i = 0
adj_i = 0
col_i = 0
ani_i = 0
numbers = numbers[:-1]
adjectives = adjectives[:-1]
colors = colors[:-1]
animals = animals[:-1]

while (True):
    if (num_i < len(numbers) - 1):
        num_i += 1
    else:
        if (adj_i < len(adjectives) - 1):
            adj_i += 1
            num_i = 0
        else:
            if (col_i < len(colors) - 1):
                col_i += 1
                adj_i = 0
            else:
                if (ani_i < len(animals) - 1):
                    ani_i += 1
                    col_i = 0
                else:
                    break

    a = numbers[num_i]
    b = adjectives[adj_i]
    c = colors[col_i]
    d = animals[ani_i]
    print a + b + c + d
    if (hashlib.md5(a + b + c + d).hexdigest() == "f54f10fd6e38929084d505d0c2e9c997"):
        print numbers[num_i] + adjectives[adj_i] + colors[col_i] + animals[ani_i]
        print "DONE"
        sys.exit(0)


