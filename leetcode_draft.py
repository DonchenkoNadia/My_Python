s = "PAYPALISHIRING"
numRows = 4
ans = [["0", "0", "0", "0"],
       ["0", "0", "0", "0"],
       ["0", "0", "0", "0"],
       ["0", "0", "0", "0"] ]
ch = 0



for i in range (0, numRows):
    ans[i][0] = s[ch] if ch > 0 else "*"
    ch += 1

i = numRows - 1
while i > 1:
    ans[i-1][numRows - i] = s[ch] if ch > 0 else "*"
    ch += 1
    i -= 1

for i in range (0, numRows):
    ans[i][numRows-1] = s[ch] if ch > 0 else "*"
    ch += 1


for i in ans:
    print (i)

print(len(s))
