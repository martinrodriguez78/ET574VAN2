#A
print(str0[0])
print(str0[-1])
print(str0[:])
print(str0[0], str0[-1],
str0[:], sep = ' '

#B
print('C'[0])
print("C"[-1])
print('C'[:])
print('C'[0], 'C'[-1],
'C'[:], sep = '\t')

#C
str1 = “coDE”
print(str1.capitalize()+'\n'+str1.upper()+'\n'+str1.lower())
print(str1)

#D
str2 = "computer science"
print(str2.title(),'|',str2[0:8],'|',str2[:3],'|',
str2[-5:-1], '|', str2[-2:] )
print(str2.title(), str2[0:8], str2[:3],
str2[-5:-1], str2[-2:], sep = ' | ')

#E
str3 = "mississippi"
print("i =",str3.count('i'))
print("s = index[", str3.find('s'), ']')
print('p = ', str3.rfind('p'))
print("Miss = ", str3.find("Miss")

#F
str4 = " Today's program "
print('lstrip():',str4.lstrip())
print('rstrip():',str4.rstrip())
print('strip():',str4.strip() + " – Basic IO")

#G
print("Price: ", '$', 19.99)
print("Price: ", '$', 19.99, sep = '')

#H 
print('Py', 'th', 'on', sep = '')
print('Py', 'th', 'on', sep = '\t')
print('Py', 'th', 'on', sep = '\n')

#I 
print('tic', 'tac', 'toe', sep = '-', end = ' ')
print("game starts", end = '!\n')
print('in'.title(), 'person'.capitalize(), sep = '-', end = ' ')
print('tutoring'.upper()

#J
print("Number\tSquare")
print(str(2) + '\t' + str(2**2))
print(str(3) + '\t' + str(3**2))
print(2, '\t', 2**2)
print(3, '\t', 3**2)

#K
print("STATE\tCAPITAL".expandtabs(15))
print('North Dakota\tBismarck'.expandtabs(15))
print('South Dakota\tPierre'.expandtabs(15))
print('Ohio\tColumbus'.expandtabs(15))
print('North Dakota\tBismarck')
print('South Dakota\tPierre')
print('Ohio\tColumbus')