#70. Climbing Stairs
#Base cases:
#if n <= 0, then the number of ways should be zero.
#if n == 1, then there is only way to climb the stair.
#if n == 2, then there are two ways to climb the stairs.
#One solution is one step by another; the other one is two steps at one time.

#The key intuition to solve the problem is that given a number of stairs n, if we know the number ways to
#get to the points [n-1] and [n-2] respectively, denoted as n1 and n2 , then the total ways to
#get to the point [n] is n1 + n2. Because from the [n-1] point, we can take one single step to
#reach [n]. And from the [n-2] point, we could take two steps to get there.

#good test cases are here https://leetcode.com/problems/string-to-integer-atoi/discuss/748024/Python3-solution-with-a-Process-for-coding-interviews
s = "-2147483649"
sign = 1
ans = 0
num_begin = 0
num_end = len(s)

for i, val in enumerate(s):
    if val == " ":
        continue
    elif val == "-":
        sign = -1
    elif val == "+":
        sign = 1
    elif val in "0123456789":
        num_begin = i
        break

for i, val in enumerate(s[num_begin:]):
    if val in "0123456789":
        continue
    else:
        num_end = i
        break
print(num_begin)
print(num_end)

#print(len(s)-num_end)
ans = (int(s[num_begin:]))*sign
if ans > 2147483647:
    ans = 2147483648
if ans < -2147483648:
    ans = -2147483648
print(ans)
