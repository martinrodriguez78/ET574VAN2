n = []
 #first bracket
n.append(2)
n.append(4)
print(n)
 
n.insert(0, 0)
n.insert(1, 1)
n.insert(2, 3)
print(n)
 
n.append(5)
print(n)

 #first removal 
n.remove(0)
print(n)
 
 #pop will remove it from the list and display it on outside. 
removed2 = n.pop(n.index(2))
print(removed2)
print(n)
 
removed4 = n.pop(n.index(4))
print(removed4)
print(n)
 
print(0 + removed2 + removed4)
 
n[0] = 100
n[-1] = 9.9
 
newNum = n.copy()
n.clear()
 
print([100, 1, 3, 5, 9.9])  # original list state before clear
print("original list = " + str(n))
print("New List = " + str(newNum))
 
del n