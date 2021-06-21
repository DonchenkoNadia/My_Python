a = int(input())
b = int(input())

#YES, if true

#a = {xyxyyx}
#b = {xyyxyx}

len_a = a.bit_length()
len_b = b.bit_length()
i = 0

def get_normalized_bit(value, bit_index):
    return (value >> bit_index) & 1

def Check(a, b):
    if len_a != len_b:
        #print ("NO")
        return 0

    for i in range(0, len_a // 2 + 1):
        if get_normalized_bit(a, len_a - i - 1) != get_normalized_bit(b, i):
            #print("NO")
            return 0
    return 1

if Check(a, b):
    print("Yes")
else:
    print("No")
