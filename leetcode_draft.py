chars = ["a","a","a","b","b","a","a"]
tmp_chars = []
index = 0
i = 0
while i < len(chars):
    j = i
    while j < len(chars) and chars[j] == chars[i]:
        j += 1
    tmp_chars.append(chars[i])
    index += 1

    if j - i > 1:
        count = j - i

        temp_lst = list(str(count))

        l = 0
        while l < len(temp_lst):
            index += 1

            tmp_chars.append(temp_lst[l])
            #chars[index] = temp_lst[l]
            l += 1
    i = j
chars = tmp_chars
print (chars)
print(index)
