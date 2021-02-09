def lastElement(x):
    return x[-1]

def firstElement(x):
    return x[0]

def lastAndFirstElements(x):
    return (x[-1], x[0])

def sortText(string):
    for i in "aeiouAEIOU" :
        string = string.replace(i, '')
    string = sorted(string)
    return list(string)

def sortList(list):
    list = sorted(list)
    print(list)
    list = sorted(list, reverse=True)
    print(list)
    list = sorted(list, key=len)
    print (list)
    list = sorted(list, key=lastElement)
    print(list)

def filePrint(fileName):
    f = open(fileName)
    print(f.read())
    f = open(fileName)
    print(f.readline())
    f = open(fileName)
    print(f.readlines())

def sortingTuples(list):
    list = sorted(list, key=lastAndFirstElements)
    return list

unsortedString = "Alex has many apples"
listOfNames = ["Claus", "Ib", "Per"]
fileName = "songs.docx"
listOfTuples = [(1,2),(2,2),(3,2),(2,1),(2,2),(1,5), (10,4), (10, 1), (3, 1)]

print(sortText(unsortedString))
sortList(listOfNames)
filePrint(fileName)
print(sortingTuples(listOfTuples))






