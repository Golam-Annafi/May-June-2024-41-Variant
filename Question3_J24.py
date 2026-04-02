#3.a 
global QueueData
global QueueHead
global QueueTail
QueueData = [""] * 20
QueueHead = -1
QueueTail = -1

#3.b EnQueue
def Enqueue(data):
    global QueueData
    global QueueHead
    global QueueTail 
    if QueueTail == 19:
        return False
    elif QueueHead == -1:
        QueueHead = 0
    QueueTail += 1
    QueueData[QueueTail] = data
    return True

#3.c 
def Dequeue(): 
    global QueueData
    global QueueHead
    global QueueTail
    if QueueTail == -1 or QueueHead == -1:
        return False
    else:
        returned_val = QueueData[QueueHead]
        if QueueHead == QueueTail:
            QueueHead = -1
            QueueTail = -1
        else:
            QueueHead += 1
        return returned_val 
    
#3.d.i 
def StoreItems():
    global QueueData
    global QueueHead
    global QueueTail
    invalid = 0
    
    for i in range(0,10):
        data = input("Enter a 7-character input: ")
        total = (int(data[0]) * 1) + (int(data[1]) * 3) + (int(data[2]) * 1) + (int(data[3]) * 3) + (int(data[4]) * 1) + (int(data[5]) * 3) 
        
        check_digit = total // 10
        if check_digit == 10:
            final_check = "X"
        else:
            final_check = str(check_digit)
        if final_check == data[6]:
            result = Enqueue(data[0:6])
            if result == True:
                print("Value Inserted")
            else:
                print("Queue Full")
        else:
            invalid += 1
    print(f"There were {invalid} invalid number(s)")
    
#3.d.ii 
StoreItems()
result = Dequeue()
if result == False:
    print("Queue Empty")
else:
    print(result)