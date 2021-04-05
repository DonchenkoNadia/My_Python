import heapq

li = [5, 7, 9, 1, 3]
print(li)

heapq.heapify(li)
print ("The created heap is : ")
print(list(li))

heapq.heappush(li, 4)
print ("The modified heap after push is : ")
print(list(li))

print ("The popped and smallest element is : ")
print (li[0])

print ("The modified heap after popping is : ")
print(list(li))
