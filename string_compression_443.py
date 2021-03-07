#https://leetcode.com/problems/string-compression/ 
chars = ["a","a","b","b","c","c","c"]
i = 0
to = 0
while i < len(chars)-1:
    j = i
    while j < len(chars) and chars[j] == chars[i]:
        j += 1

    num = j - i
    chars[to] = chars[i]
    to += 1
    if num > 1:
        for digit in str(num):
            chars[to] = digit
            to += 1
    i = j
chars = chars[:to]
print(chars)
print(to)
