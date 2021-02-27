n = 4
a = [57, 57, -57, 57]
maximum = -100
second_maximum = -100

for i in range(len(a)):
    if a[i] > maximum:
        maximum = a[i]
for i in range(len(a)):
    if a[i] > second_maximum and a[i] < maximum:
        second_maximum = a[i]

print("maximum = ", maximum)
print("second_maximum = ", second_maximum)
