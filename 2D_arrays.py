a = [[1, 2, 3, 4],
     [5, 6],
     [7, 8, 9]]
print ("Number of rows: ")
rows = len(a)
print (rows)
print("Number of columns ")
print (len(a[0]))

for i in range(len(a)):
    for j in range(len(a[i])):
        print(f'a[{i}][{j}] = {(a[i][j])} ')
