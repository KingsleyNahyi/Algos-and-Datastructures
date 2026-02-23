#stacks work with last in first out 
#it's like having plates stacked on top of each other you can only remove from the top not the bottom so the first thing you placed at the bottom is the last you can remove 
#core operations 
  #adding on to the stack 
  #removing from the stack 
  #peeking to see whats at the top of the stack. 


stack = [] 
f = "nothing"

stack.append(f)
stack.pop() 
stack[-1]
len(stack)==0 


def isValid(s):
    stack = []
    mapping = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in s:
        if char in mapping:  # closing bracket
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:  # opening bracket
            stack.append(char)

    return len(stack) == 0


#next greater element (monotonic stack)

def next_greate(nums):
   n = len(nums)
   res = [-1]*n 
   stack = []

   for i, num in enumerate(nums):
       while stack and nums[stack[-1]]<num: 
           idx = stack.pop()
           res[idx]= num 
       stack.append(i)
      
   return res