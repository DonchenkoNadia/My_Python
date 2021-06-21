'''
a = int(input())
b = int(input())
print(f"You have entered a = {a}")
print(f"You have entered b = {b}")
print("   ")
print(f"bin repr of a - {bin(a)}")
print(f"bin repr of b - {bin(b)}")
len_a = a.bit_length()
len_b = b.bit_length()
print(f"a.bit_length() = {len_a}")
print(f"b.bit_length() = {len_b}")

n = 5
nums = [7, 1, 1, 4, 5, 7]
res = 0
for i in nums:
    res = res ^ i
print(f"res = {res}")
#подумать про два непарных элемента
'''

a = 146
def get_normalized_bit(value, bit_index):
    return (value >> bit_index) & 1

def set_bit(value, bit_index):
    return value | (1 << bit_index)

def clear_bit(value, bit_index):
    return value & ~(1 << bit_index)

len_a = a.bit_length()
one_counter = 0
zero_counter = 0

for i in range(0, len_a):
    if get_normalized_bit(a, i) == 1:
        one_counter += 1
    else:
        zero_counter += 1

print(f"bin(a) = {bin(a)}")
print(f"one_counter = {one_counter}")
print(f"zero_counter = {zero_counter}")

ans = 0

n = set_bit(0,2)
for i in range(0, one_counter + zero_counter):
    ans = set_bit(ans, i)
for i in range(0, zero_counter):
    ans = clear_bit(ans, i)

print(f"bin(a) = {bin(a)}")
print(f"bin(ans) = {bin(ans)}")
print(f"ans = {ans}")
