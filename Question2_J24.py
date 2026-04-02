#2.a.i
class Tree:
    def __init__(self, aname, agrowth, aheight, awidth, aevergreen):
        self.__TreeName = aname      #string
        self.__HeightGrowth = agrowth   #integer
        self.__MaxHeight = aheight    #integer
        self.__MaxWidth = awidth      #integer
        self.__Evergreen = aevergreen  #string
        
#2.a.ii
    def GetTreeName(self):
        return self.__TreeName
    def GetGrowth(self):
        return self.__HeightGrowth
    def GetMaxHeight(self):
        return self.__MaxHeight
    def GetMaxWidth(self):
        return self.__MaxWidth
    def GetEverGreen(self):
        return self.__Evergreen
    
#2.b 
def ReadData(): 
    TreeObjects=[] 
    try: 
        File = open("Trees.txt") 
        TreeData = [] 
        TreeData = File.read().split("\n") 
        SplitTrees = [] 
        for Item in TreeData: 
            SplitTrees.append(Item.split(",")) 
        File.close() 
        for Item in SplitTrees: 
            TreeObjects.append(Tree(Item[0],int(Item[1]),int(Item[2]),int(Item[3]),Item[4])) 
    except IOError: 
        print ("invalid file") 
    return TreeObjects

#2.c 
def PrintTrees(Tree):
    if Tree.GetEverGreen() == "No":
        output = "It loses its leaves each year"
        print(f"{Tree.GetTreeName()} has a maximum height {Tree.GetMaxHeight()} a maximum width {Tree.GetMaxWidth()} and grows {Tree.GetGrowth()} cm a year. {output}")
    else:
        output = "It does not lose its leaves"
        print(f"{Tree.GetTreeName()} has a maximum height {Tree.GetMaxHeight()} a maximum width {Tree.GetMaxWidth()} and grows {Tree.GetGrowth()} cm a year. {output}")
#2.d.i      
returned = ReadData()
for i in returned:
    PrintTrees(i)
    
#2.e 
def ChooseTrees(Trees):
    Height = int(input("Enter tree height you require(in cm): "))
    Width = int(input("Enter tree width you require(in cm): "))
    Evergreen = input("Yes for evergreen/No for not evergreen: ")
    
    if Evergreen.lower() == "yes":
        Keep = "Yes"
    else:
        Keep = "No"
    options = []
    for items in Trees:
        if items.GetMaxHeight() <= Height and items.GetMaxWidth() <= Width and items.GetEverGreen() == Keep:
            options.append(items)
            PrintTrees(items)
    if len(options) == 0:
        print("No suitable tree available")
        
#2.e.ii 
     
    Valid = False 
    while Valid == False: 
        Choice = input("Enter the name of the tree you want: ") 
        for Item in options: 
            if Item.GetTreeName() == Choice: 
                Valid = True 
                Selected = Item 
                Start = int(input("Enter the height of the tree you would like to start with in cm: ")) 
                Years =  (Selected.GetMaxHeight() - Start)/Selected.GetGrowth() 
                print("Your tree should be full height in approximately", Years,"years") 
    
#2.e.iii   
ChooseTrees(returned)