#Задачка с разворотом строки
s = ["1", "2", "3", "4", "5"]
if not s:
    print("schade")
left = 0
right = len(s) - 1
print("right ", right)
while left < right:
    s[left], s[right] = s[right], s[left]
    left += 1
    right -= 1
print (s)
