
#bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

#selection sort 
def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # Assume the current i is the min
        min_idx = i
        
        # Find the minimum element in the unsorted part
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum with the first unsorted element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

#insertion sort 
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # the element to insert
        j = i - 1
        
        # Move elements of arr[0..i-1], that are greater than key, one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # shift element right
            j -= 1
        
        arr[j + 1] = key  # insert key in correct position
    return arr


#EFFICIENT SORTING ALGORITHMS 
#merge sort 
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    # Merge two sorted arrays
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Append remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

#quick sort 
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]  # pick last element as pivot
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    
    return quick_sort(left) + [pivot] + quick_sort(right)

def counting_sort(arr, max_val):
    # 1) Create a frequency array of size max_val + 1 (to include max_val index)
    count = [0] * (max_val + 1)

    # 2) Count occurrences of each value in arr
    for num in arr:
        count[num] += 1

    # 3) Reconstruct the sorted array using counts
    result = []
    for value in range(len(count)):
        # Append 'value' exactly 'count[value]' times
        result.extend([value] * count[value])

    return result