import math


#linear search 

def linear_search(arr,target):
  """
 Time complexity: O(n)
 Space complexity: O(1)

 Works on: any array(sorted or unsorted)
  
  :param arr: Description
  :param target: Description
  """

  for i, element in enumerate(arr):
    if element== target: 
      return i 
    
  return -1 

#to return all occurences 
  indices = []

  for i in len(arr):
    if element ==target:
      indices.append(i)


#binary search divide and conquer algorithm works on sorted arrays 
#hear you have a left and right and middle you check to see if the middle is equall to the target if the middle is less than the target you add 1 to the left 
#after adding one to the left you recalibrate your mid and check again 
#if the opposite is true you subtract one from the right.
# time complexity is O(logn)
# space complexity is O(1) 
def binary_search(arr, target):
  left, right = 0, len(arr)-1

  while left<=right: 
    mid = (left + right)//2

  if arr[mid] == target: 
    return mid 
  elif arr[mid]<target: 
    left = mid +1 
  else: right = mid - 1

  return -1


#JUmp search works on sorted arrays. 
#instead of checking every element it jumps ahead by a fixed number of steps/
#it jumps till the target is less than the element and then you check the previous block and apply linear search.
#best case time complexity is O(1)
#worst case is O(root n)
#space complexity is O(1) few variables.

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    # Jump ahead by steps
    while prev < n and arr[min(step, n)-1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    # Linear search in block
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1




#interpolation search also works for uniformly distributed sorted arrays 
#best case is O(1)
#average is case is O(log log n) if values are uniformly distributed
#worst case is O(n) if values are unevenly distributed
def interpolate(arr, target):
   low,high = 0, len(arr)-1

   while low<=high and arr[low]<=target<=arr[high]:
      if arr[low] == arr[high]:
         if arr[low] == target:
            return low 
         else: 
            return -1
         
      pos = low + ((target-arr[low])*(high-low))//(arr[high]-arr[low])
      if arr[pos] ==target: 
         return pos 
      elif arr[pos]<target: 
         low = pos +1 
      else: 
         high = pos - 1




#exponential search works for unbounded/infinite sorted arrays or when target is near beginning 
#here you jump like interpolation but you jump to where you think the target might be 
#then you do a binary search in the range. 
#

def exponential_search(arr, target):
    if arr[0] == target:
        return 0

    n = len(arr)
    i = 1
    while i < n and arr[i] <= target:
        i *= 2

    # binary search in found range
    left = i // 2
    right = min(i, n - 1)
    return binary_search(arr, target, left, right)

def binary_search(arr, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

#ternary search. Similar to binary search but divides array into 3 parts. 
