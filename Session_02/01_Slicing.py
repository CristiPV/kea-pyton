#['Hello', 'World', 'Huston', 'we', 'are', 'here'] should become -> ['World', 'Huston', 'we', 'are']
#['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['Hello', 'World']
#['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['are', 'here']
#['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['are']
#['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['Hello', 'Huston', 'are']
#['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['here', 'are', 'we', 'Huston', 'World', 'Hello']
#('Hello', 'World', 'Huston', 'we', 'are', 'here') should become -> ['World', 'Huston', 'we', 'are']
#'Hello World Huston we are here' -> 'World Huston we'

initialList = ['Hello', 'World', 'Huston', 'we', 'are', 'here']
initialTuple = ('Hello', 'World', 'Huston', 'we', 'are', 'here')
initialString = 'Hello World Huston we are here'

list1 = initialList[1:5]
print(list1)

list2 = initialList[:2]
print(list2)

list3 = initialList[-2:]
print(list3)

list4 = initialList[-2:-1]
print(list4)

list5 = initialList[::2]
print(list5)

list6 = initialList[::-1]
print(list6)

tuple = list(initialTuple[1:5])
print(tuple)

string = initialString[5:21]
print(string)