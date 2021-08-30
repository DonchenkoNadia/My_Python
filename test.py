#куча задач на посчитай варианты чего то в строке решается динамикой по балансу(сам недавно узнал)
'''
fin  = open("input.txt")
fout = open("output.txt","w")

s = fin.readline()
print(s)
'''
s = "????"
n = len(s)
print(n)

s = " " + s

dp = [[ 0 for i in range(0, n+1)] for j in range(0, n+1)]

dp[0][0] = 1

for lang in range(1, n+1):
	for open in range(0, n+1):
		if open - 1 >= 0 and (s[lang] == "?" or s[lang] == "("):
			dp[lang][open] += dp[lang-1][open-1]
		if open + 1 <= n and (s[lang] == "?" or s[lang] == ")"):
			dp[lang][open] += dp[lang-1][open+1]

print(f"answer = {dp[n][0]}")

'''
fout.write(str(dp[n][0]))

fin.close()
fout.close()
'''
