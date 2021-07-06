fin  = open("input.txt")
fout = open("output.txt","w")

s = fin.readline()

def prefix(s):
    l = len(s)
    pi = [0]
    k = 0
    for i in range(1, l-1):
        while(k > 0 and s[k] != s[i]):
            k = pi[k-1]
        if (s[k] == s[i]):
            k = k+1
        pi.append(k)
	#print "pattern is: ", p
	#print "pi values are: ", pi
    return pi

ans = ""
pi = prefix(s)
print(pi)
print(len(pi))
print(s)
print(len(s))

for i in pi:
    ans += str(i)
    ans += " "

fout.write(ans)

fin.close()
fout.close()
