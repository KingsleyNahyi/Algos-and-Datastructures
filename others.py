#palindrom check 
def is_palindrome(s):
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

#checking for duplicates 
def remove_duplicates(nums):
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1

#maximum subarray 
def maxSubArray(nums):
    currentSum = nums[0]
    maxSum = nums[0]

    for i in range(1, len(nums)):
        currentSum = max(nums[i], currentSum + nums[i])
        maxSum = max(maxSum, currentSum)

    return maxSum

#two sum 
def twoSum(nums, target):
    num_map = {} 

    for i,num  in enumerate(nums): 
	    complement = target - num 
	    if complement in num_map: 
		    return [num_map[complement], i]
	    num_map[nums] = i 
         
#length of longest substring 
def length_of_longest_substring(s):
    char_map = {}  # char -> last index seen
    left = 0       # start of current window
    max_len = 0

    for right, char in enumerate(s):
        if char in char_map and char_map[char] >= left:
            # move left pointer past the previous occurrence
            left = char_map[char] + 1
        # store/update the index of the current character
        char_map[char] = right
        # update max length
        max_len = max(max_len, right - left + 1)

    return max_len

# Example
print(length_of_longest_substring("abcabcbb"))  # 3

def subarray_sum(nums, k):
    # Initialize hashmap with 0 sum seen once
    prefix_count = {0: 1}

    current_sum = 0  # running sum of elements
    count = 0        # number of subarrays summing to k

    for num in nums:
        current_sum += num  # add current number to running sum

        # Check if there is a prefix sum that satisfies: current_sum - prefix_sum = k
        # Rearranged: prefix_sum = current_sum - k
        if current_sum - k in prefix_count:
            count += prefix_count[current_sum - k]  # add how many times we've seen that sum

        # Record the current prefix sum in the hashmap
        if current_sum in prefix_count:
            prefix_count[current_sum] += 1
        else:
            prefix_count[current_sum] = 1

    return count

# Example usage
nums = [1, 2, 3]
k = 3
print(subarray_sum(nums, k))  # Output: 2
