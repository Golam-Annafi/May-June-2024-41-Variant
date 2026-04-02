Question 1: 
Core concept(s): 1D Arrays, BubbleSorting, binarySearch
This Question is designed to take raw sets of integers into an array, sort them in ascending order and then
allow users to quickly locate their desired number inside the array using BinarySearch. This teaches the foundation
of every irl database systems. Sorting data makes it more readable and BinarySearching allows for numbers to be accessed
quickly especially if there's thousands of numbers.

 Part 1(a): Declare global array 'DataStored' (20 integers) and 'NumberItems' (item count).

 Part 1(b): Initialise() function:
 1. Input quantity of numbers (validate between 1 and 20).
 2. Input each number and store it in 'DataStored'.

 Part 1(c): Main program to set NumberItems to 0, call Initialise(), and print the array.

 Part 1(d): BubbleSort() procedure to sort 'DataStored' into ascending order.
 Amend main program to call BubbleSort() and output the sorted array.

 Part 1(e): Iterative BinarySearch(DataToFind) function:
 1. Search 'DataStored' for the parameter.
 2. Return the index if found, else return -1.
 Amend main program to take user input, call the search, and print the result.


Question 2:
Core Concepts: Object-Oriented Programming (OOP), File Handling (Reading .txt), Exception Handling, Logic Filtering.
This question is designed to create an object using class structure, populate it from an external file (Trees.txt) and
provide a "recommendation" to the user based on their requirements. This mimics real-world e-commerce or inventory apps. 
OOP allows you to bundle the data (height, width) with the logic (printing details) into one clean package, making the code easy to scale and maintain.

 Part 2(a)(i): Declare class 'Tree' with private attributes and Constructor.
 Part 2(a)(ii): Create Get methods for all attributes (TreeName, Growth, Heights, etc.).

 Part 2(b): ReadData() function: 
 1. Open 'Trees.txt', handle exceptions if file not found.
 2. Read lines, create 'Tree' objects, and return an array of objects.

 Part 2(c): PrintTrees(TreeObject) procedure:
 Format and output tree details based on whether it is evergreen or not.

 Part 2(d): Main program to call ReadData() and print details of the first tree.

 Part 2(e)(i): ChooseTree(TreeArray) procedure:
  1. Input user requirements (Max Height, Max Width, Evergreen).
  2. Filter and print trees that meet all three criteria.
 Part 2(e)(ii): Amend ChooseTree() to:
  1. Input a chosen tree name and its starting height.
  2. Calculate years to reach MaxHeight: (Max - Current) / Growth.

Question 3:
Core Concepts: Abstract Data Types (Linear Queue), Check Digit Algorithms (Data Integrity), String Manipulation.
This question is designed To create an Queue that only accepts "clean" data by calculating a mathematical checksum for every input 
before it’s allowed into memory.
In the real world, this is how credit card numbers or ISBNs are validated. The queue ensures that data is processed
in the exact order it was received (First-In-First-Out), which is vital for things like printer spoolers or bank transaction processing.

 Part 3(a): Main program setup:
  1. Declare 'QueueData' (1D array of 20 strings) with null values.
  2. Initialize 'QueueHead' and 'QueueTail' to -1.

 Part 3(b): Enqueue(data) function:
   1. Check if queue is full.
   2. Update pointers and add data to the tail.
   3. Return True if successful, False if full.

 Part 3(c): Dequeue() function:
   1. Check if queue is empty (return "false").
   2. Extract item from head and update pointers (handle reset to -1).
   3. Return the extracted value.

Part 3(d)(i): StoreItems() subroutine:
   1. Take 10 inputs and calculate the check digit (multiplier 1,3 logic).
   2. If valid (matching 7th char), Enqueue the first 6 digits and print status.
   3. If invalid, increment counter. Output total invalid count at the end.

 Part 3(d)(ii): Amend main program:
 Call StoreItems(), then call Dequeue() once and output result or "Empty" message.
