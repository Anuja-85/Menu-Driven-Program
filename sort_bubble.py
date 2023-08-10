# Method 1
# Optimized Python program for implementation of Bubble Sort
def bubbleSort(arr):
    n = len(arr)
      
    # Traverse through all array elements
    for i in range(n):
        swapped = False
  
        # Last i elements are already in place
        for j in range(0, n-i-1):
  
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break
  
  
# Driver code to test above
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
  
    bubbleSort(arr)
  
    print("Sorted array:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")
        
        
# Method 2

# Creating a bubble sort function  
def bubble_sort(list1):  
    # Outer loop for traverse the entire list  
    for i in range(0,len(list1)-1):  
        for j in range(len(list1)-1):  
            if(list1[j]>list1[j+1]):  
                temp = list1[j]  
                list1[j] = list1[j+1]  
                list1[j+1] = temp  
    return list1  
  
list1 = [64, 34, 25, 12, 22, 11, 90]  
print("The unsorted list is: ", list1)  
# Calling the bubble sort function  
print("The sorted list is: ", bubble_sort(list1))  

#Method 3

# Creating a bubble sort function  
def bubble_sort(list1):  
    # Outer loop for traverse the entire list  
    for i in range(0,len(list1)-1):  
        for j in range(len(list1)-1):  
            if(list1[j]>list1[j+1]):
                list1[j],list1[j+1] = list1[j+1], list1[j]  
    return list1  
  
list1 = [64, 34, 25, 12, 22, 11, 90]  
print("The unsorted list is: ", list1)  
# Calling the bubble sort function  
print("The sorted list is: ", bubble_sort(list1)) 

# We can prevent the unnecessary evaluation using the Boolean flag and checks if any swaps were made in 
# the previous section.

def bubble_sort(list1):  
   # We can stop the iteration once the swap has done  
    has_swapped = True  
  
    while(has_swapped):  
        has_swapped = False  
        for i in range(len(list1) - 1):  
            if list1[i] > list1[i+1]:  
                # Swap  
                list1[i], list1[i+1] = list1[i+1], list1[i]  
                has_swapped = True  
    return list1  
  
list1 = [64, 34, 25, 12, 22, 11, 90]  
print("The unsorted list is: ", list1)  
# Calling the bubble sort function  
print("The sorted list is: ", bubble_sort(list1))  