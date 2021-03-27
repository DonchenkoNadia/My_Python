arr = [1,4,2,5,3]
sum = 0
i = 0
while i <= len(arr):
    j = i
    while j <= len(arr):
        k = i
        if (j - k) % 2 == 1:
            while k < j:
                sum += arr[k]
                k += 1
        j += 1
    i += 1
print(sum)
