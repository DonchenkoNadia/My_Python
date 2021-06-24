'''
Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
'''
def get_normalized_bit(value, bit_index):
    return (value >> bit_index) & 1

a = 3
b = 1

len = max(a.bit_length(), b.bit_length())
#print(len)

first_dif = 0
first_bit = 0

second_bit = 0

for i in range(0, len):
    if ((get_normalized_bit(a, i) != get_normalized_bit(b, i)) and first_dif == 0):
        first_bit = i
        first_dif = 1
    if ((get_normalized_bit(a, i) != get_normalized_bit(b, i)) and first_dif == 1):
        second_bit = i

#print(f"first_bit = {first_bit}")
#print(f"second_bit = {second_bit}")

print(mod(second_bit-first_bit))
