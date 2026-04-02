#1.a
DataStored = []
NumberItems = 0

#1.b 
def Initialise():
    global DataStored
    global NumberItems
    Valid = False
    while not Valid:
        NumberItems = int(input("How many numbers would u like to enter(1-20)?: "))
        if NumberItems >=1 and NumberItems <=20:
            Valid = True
        else:
            print("Number must be between 1 and 20")
    for x in range(0, NumberItems):
        DataStored.append(int(input("Enter num: ")))
        
#1.c.i 
NumberItems = 0
Initialise()
print(DataStored)

#1.d.i
def BubbleSort():
    global DataStored
    global NumberItems
    temp = 0
    for x in range(0, NumberItems):
        for y in range(0, NumberItems - x - 1):
            if DataStored[y] > DataStored[y+1]:
                temp = DataStored[y+1]
                DataStored[y+1] = DataStored[y]
                DataStored[y] = temp

#1.d.ii 
BubbleSort()
print(DataStored)

#1.e.i 
def BinarySearch(DataToFind):
    global DataStored
    global NumberItems
    First = 0
    Last = NumberItems - 1
    while First <= Last:
        mid = (First+Last) // 2
        if DataStored[mid] == DataToFind:
            return mid
        else:
            if DataStored[mid] < DataToFind:
                First = mid + 1
            elif DataStored[mid] > DataToFind:
                Last = mid - 1
    return -1

#1.e.ii 
Data = int(input("What number do u wish to find?: "))
print(BinarySearch(Data))