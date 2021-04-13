num1 = "123"
num2 = "456"
subtotal = []
total = ""
i = len(num2) - 1
remainder = 0
while i >= 0:
    cursubtotal = ""
    j = len(num1) - 1
    while j >= 0:
        cursubtotal += str((int(num1[j])*int(num2[i]))%10 + remainder)
        remainder = (int(num1[j])*int(num2[i]))//10
        j -= 1
    subtotal.append(cursubtotal[::-1])
    i -= 1
print(subtotal)
for sb in subtotal:
    print(sb)
