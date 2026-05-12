n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#A
print(n, n[:])#prints the entire list twice
print(n[0], n[-10]) #prints the first element of the list 
print(n[9], n[-1])#prints the last element of the list
print(n[3:])#prints the list starting from the fourth element to the end
print(n[:5]) #prints the list starting from the beginning to the fifth element (not including the fifth element)
print(n[3:7])#prints the list starting from the fourth element to the seventh element (not including the seventh element)
n.insert(3, "banana")#inserts "banana" at index 3 (Fourth element)
n.insert(-1, "kiwi") #inserts "kiwi" at index -1 (second to last element)
print(n) #prints the updated list
#print(f"Do you like {str(n[0].upper())} or {str(n[-1].upper())}?") #prints a question asking if the user likes the first or last element of the list, with the elements in uppercase
print(n[-5:-1]) #prints the list starting from the fifth to last element to the second to last element (not including the second to last element)
print(n[4:8]) #prints the list starting from the fifth element to the eighth element (not including the eighth element)

#B
print(n[-1] + n[-2]) #prints the sum of the last two elements of the list
print(n[9] - n[1]) #prints the difference between the last element and the second element of the list
print(n[2] * n[5])#prints the product of the third element and the sixth element of the list
print(n[8] / n[2]) #prints the quotient of the ninth element and the third element of the list
print(len(n), n[:len(n)], sep = '\n') #prints the length of the list and the entire list on a new line
print(min(n), max(n), type(n), sep = '\t') #prints the minimum and maximum values of the list, as well as the type of the list, separated by a tab

#C
n[0], n[9] = "apple", 'cherry' #replaces the first element with "apple" and the last element with "cherry"
n.insert(3, "banana") #inserts "banana" at index 3 (Fourth element)
n.insert(-1, "kiwi") #inserts "kiwi" at index -1 (second to last element)
print(n) #prints the updated list
print(f"Do you like {n[0].upper()} or {n[-1].upper()}?") #prints a question asking if the user likes the first or last element of the list, with the elements in uppercase

#D
n.append(-11) #adds -11 to the end of the list
n.append("orange") #adds "orange" to the end of the list
n[0], n[1] = n[-1], n[-2] #replaces the first element with the last element and the second element with the second to last element
print(n+n) #prints the list concatenated with itself
print(n*2) #prints the list repeated twice

#E
item1 = n.pop(0) #removes and returns the first element of the list, which is stored in item1
print(f"{item1} is removed.") #prints a message indicating that item1 has been removed
item2 = n.pop() #removes and returns the last element of the list, which is stored in item2
print(f"{item2} is removed.") #prints a message indicating that item2 has been removed
print('n = ', n) #prints the updated list after the removals
print(f'Removed items: {item1} & {item2}') #prints a message indicating the removed items

#F
n.insert(6, 'pear') #inserts "pear" at index 6 (seventh element)
del n[-1] #removes the last element of the list
del n[0] #removes the first element of the list
print(n) #prints the updated list after the deletions
n.remove("pear") #removes the first occurrence of "pear" from the list
n.remove(6) #removes the first occurrence of 6 from the list
print('n = ', n) #prints the updated list after the removals
n.clear() #removes all elements from the list
print(f'n = {n}') #prints the empty list after clearing all elements

#G
fruits = ['kiwi', 'pear', 'orange', 'apple', 'cherry'] #creates a list of fruits
fruits.sort() #sorts the list of fruits in alphabetical order
print(fruits[0], fruits[-1]) #prints the first and last elements of the sorted list, which are the smallest and largest fruits in alphabetical order
fruits.sort(reverse=True) #sorts the list of fruits in reverse alphabetical order
print(fruits[0], fruits[-1]) #prints the first and last elements of the reverse sorted list, which are the largest and smallest fruits in reverse alphabetical order

#H
fruits = ['kiwi', 'pear', 'orange', 'apple', 'cherry'] #creates a list of fruits
print(sorted(fruits)) #prints a new list of fruits sorted in alphabetical order, without modifying the original list
print(fruits[0], fruits[-1]) #prints the first and last elements of the original list, which are unchanged by the sorted() function
print(sorted(fruits, reverse=True)) #prints a new list of fruits sorted in reverse alphabetical order, without modifying the original list  
print(fruits[0], fruits[-1]) #prints the first and last elements of the original list, which are unchanged by the sorted() function