#31.03 I was trying to solve leetcode problem number 6 ZigZag Conversion
#Managed only to fill the matrix one time
s = "PAYPALISHIRING"
numRows = 4
ans = [["0", "0", "0", "0"],
       ["0", "0", "0", "0"],
       ["0", "0", "0", "0"],
       ["0", "0", "0", "0"] ]
ch = 0



for i in range (0, numRows):
    ans[i][0] = s[ch]
    ch += 1

i = numRows - 1
while i > 1:
    ans[i-1][numRows - i] = s[ch]
    ch += 1
    i -= 1

for i in range (0, numRows):
    ans[i][numRows-1] = s[ch] 
    ch += 1


for i in ans:
    print (i)

print(len(s))
