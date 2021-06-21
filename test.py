'''
n = 5
1 3 3 3 2
{1} {3 3 3} {2}
{1} {3 3} {3 2}

3
1 3 1
3
1 2 2

{1} {3 3 3} {2}

a = []

'''

n = 5
nums = [3, 4, 5, 6, 7, 2, 10, 11]
x = 5

amount_of_segments = 0
is_cur_segment = 0

for i in range(0, len(nums)):
    if nums[i] > x and is_cur_segment == 0:
        is_cur_segment = 1
        amount_of_segments += 1
    if nums[i] <= x and is_cur_segment == 1:
        is_cur_segment = 0
print(f"amount_of_segments = {amount_of_segments}")
