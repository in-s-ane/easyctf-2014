import string
def palin(s):
    a = 0
    max = 0
    answer = ""
    z = len(s)
    while (a < len(s)):
        while (z > a):
            if "".join([x for x in s[a:z] if x in string.ascii_letters]).lower() == "".join([x for x in s[a:z][::-1] if x in string.ascii_letters]).lower() and len("".join([x for x in s[a:z] if x in string.ascii_letters])) > max:
                answer = s[a:z]
                max = len(answer)
            z-=1
            while (s[z-1] not in string.ascii_letters):
                z-=1
        a+=1
        while (s < len(s) and s[a] not in string.ascii_letters):
            a+=1
        z = len(s)
    return answer
