digits = [9]
remainder =  1

for i in range(len(digits)-1, -1, -1):
    value = (digits[i] + remainder) % 10
    remainder = (digits[i] + remainder) // 10
    digits[i] = value

if remainder == 1:
    ans = []
    ans.append(1)
    ans += digits
    print(ans)
else:
    print(digits)
