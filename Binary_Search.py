#!/usr/bin/env python
# coding: utf-8

# In[8]:


def binarySearch (arr, L, R, x):
# If R < L then element is not present in given array 
    if R >= L: 
  #here R & L are the rightmost and leftmost elements of the array respectively

        mid = L + (R - L) // 2
  #defining mid


        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
          
        # If x is smaller than mid, then it  
        # can only be present in left subarray 
        elif arr[mid] > x: 
            return binarySearch(arr, L, mid-1, x) 
  
        # Else the element can only be present  
        # in right subarray 
        else: 
            return binarySearch(arr, mid + 1, R, x) 
  
    else: 
        # Element is not present in the array 
        return -1
  
# Example case 
arr = [ 4, 9, 22, 49, 157 ] 
x = 22
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index {} ".format(result)) 
else: 
    print ("Element is not present in array")


# In[ ]:




