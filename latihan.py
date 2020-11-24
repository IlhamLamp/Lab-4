listA = [10, 20, 30, 40, 50]
print(listA[2]) #output 30
print(listA[1:4]) #output [20, 30, 40]
print(listA[-1]) #output 50

listA[3] = 400
print(listA[3]) #output 400
listA[3:] = [4000, 500]
print(listA) #output [10, 20, 30, 4000, 500]

listB = listA[0:2]
print(listB) #output [10, 20]
listB.append('Hello')
print(listB) #output [10, 20, 'Hello']
listB.extend([15, 25, 35])
print(listB) #output [10, 20, 'Hello', 15, 25, 35]
listB = listB + listA
print(listB) #output [10, 20, 'Hello', 15, 25, 35, 10, 20, 30, 4000, 500]
