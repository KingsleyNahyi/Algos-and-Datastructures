#technique where you use two indices to traverse a data structure 
#it reduces complexities from O(n2) to O(n)

##one from left one for right 
##used when stuff is sorted already 
#used in two sum, reversing an array, checking palindrome, and removing duplicate 

#reversa; pf ;ost
def reverse(arr):
  left = 0 
  right = len(arr)-1 

  while left<right: 
    arr[left],arr[right] = arr[right],arr[left]
    left+=1
    right-=1
  

#plaindrome check 
def isapalindrome(arr):
  left = 0 
  right = len(arr)-1 

  while left<right: 
    if arr[left]!=arr[right]:
      return False 
    left+=1 
    right-=1 
  return True

#two sum 
def twosum(arr,k):
  left = 0 
  right = len(arr)-1 

  while left<right: 
    sum = arr[left]+ arr[right]
    if sum==k: 
      return arr[left],arr[right]
    if (sum<k): 
      left+=1 
    else: 
      right-=1 

  return -1 
  
#removing duplicates 
def duplicates(arr):
  left = 0 

  for right in range(1, len(arr)):
    if arr[left]!=arr[right]:
      left+=1 
      arr[left]= arr[right]


