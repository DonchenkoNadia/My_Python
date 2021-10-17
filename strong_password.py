def char_range(c1, c2):
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)

def countDist(s):
    ans = 0
    for i in char_range('A', 'Z'):
        ans += solve(i, s)
    return ans

def solve(c, s):
    cnt = 0
    res = 0
    for i in range(len(s)):
        if s[i] == c:
            res += cnt*((cnt + 1)/2)
            cnt = 0
        else:
            cnt += 1
    res += cnt*((cnt+1)/2)
    return len(s)*((len(s)+1)/2) - res

def findPassordStrength(password):
    return int(countDist(password))

password = "LEETCODE"
print(findPassordStrength(password))
