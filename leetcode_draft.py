M = [[0,1,1,0],
     [0,1,1,0],
     [0,0,0,1]]

if len(M) == 0:
    print("It is a mistake")
max_number_of_ones = 0
#let's start with horisontal line
for row in M:
    count = 0
    for elem in row:
        if elem == 1:
            count += 1
            max_number_of_ones = max(max_number_of_ones, count)
        else:
            count = 0
#now let's check vertical
for i in range(0, len(M[0])):
    count = 0
    for j in range(0, len(M)):
        #print (f"M[{j}][{i}] = {M[j][i]}")
        if M[j][i] == 1:
            count += 1
            max_number_of_ones = max(max_number_of_ones, count)
        else:
            count = 0
#upper-diagonal
