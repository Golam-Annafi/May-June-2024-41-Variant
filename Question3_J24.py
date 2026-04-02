#3.a 
QueueData = []
for x in range(0,20):
    QueueData.append("")
QueueHead = -1
QueueTail = -1

#3.b 
def Enqueue(Data):
    global QueueData
    global QueueHead
    global QueueTail
    if QueueTail >=19:
        return False
    else:
        if QueueHead == -1:
            QueueHead = 0
        QueueTail += 1
        QueueData[QueueTail] = Data
        return True
    
#3.c 
def Dequeue():
    global QueueData
    global QueueHead
    global QueueTail
    if QueueHead == -1 or QueueHead > QueueTail:
        return False
    else:
        QueueHead += 1
        return (QueueData[QueueHead-1])
        
#3.d.i 
def StoreItems():
    invalid = 0
    for i in range(0, 10):
        values = input("Enter a 7 character string: ")
        
        sum_1 = (int(values[0]) * 1) + (int(values[2]) * 1) + (int(values[4]) * 1)
        sum_3 = (int(values[1]) * 3) + (int(values[3]) * 3) + (int(values[5]) * 3)
        
        sums = sum_1 + sum_3
        calc_digit = sums // 10 
        
        if calc_digit == 10:
            final_check = "X"
        else:
            final_check = str(calc_digit) 
        if values[6] == final_check:
            if Enqueue(values[0:6]): 
                print("Item inserted")
            else:
                print("Queue is already full")
        else:
            print("Invalid check digit")
            invalid += 1
            
    print(f"There were {invalid} invalid items")
    
#3.d.ii 
StoreItems()
result = Dequeue()
if result == False:
    print("Queue is Empty")
else:
    print(result)