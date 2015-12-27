myList = [];
for i in range(3):
	print('Enter a number:')
	myList.append(input())

myList.sort()
print(','.join(myList))
