##sliding window creates a window and uses two pointers and a condition to deal with the shrinking or the growing. 
#longest substring without repeating characters 

def longestsubstring(arr):
  left = 0 
  seen = {}
  max_len = 0 

  for right in range(len(arr)):
    while arr[right] in seen: 
      seen.remove(arr[left])
      left+=1 

    seen.add(arr[right])
    max_len = max(max_len, right-left +1 )

  return max_len


def max(s,k):
  left = 0
  freq = {}  # character → count
  max_len = 0

  for right in range(len(s),k):
      # Add s[right] to freq
      freq[s[right]] = freq.get(s[right], 0) + 1

      # Shrink window until we have at most K distinct characters
      while len(freq) > k:
          freq[s[left]] -= 1
          if freq[s[left]] == 0:
              del freq[s[left]]  # remove completely from dictionary
          left += 1

      # Update result
      max_len = max(max_len, right - left + 1)

  return max_len
