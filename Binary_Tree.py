#introduction to trees in general 
from collections import deque


class Node: 
  def __init__(self, value):
    self.value = value 
    self.left = None 
    self.right = None 


#creating a small tree 
root = Node("A")
root.left = Node("B")
root.right = Node("C")

root.left.left = Node("D")
root.left.right = Node("E")

#full binary tree has every node having either 0 or 2 children 
#complete binary tree all levels are completely filled except possibly the last. 
#perfect binary tree all nodes have two children and leaves are at the same level 
#balanced binary tree the height difference btween left and right subtrees of any node is at most 1 

#properties of binary trees 

#depth-first reversal 
#preorder 
def preorder(node):
  if node: 
    print(node.value, end = "")
    preorder(node.left)
    preorder(node.right)

#inorder 
def inorder(node):
  if node: 
    inorder(node.left)
    print(node.value, end = "")
    inorder(node.right)

def postorder(node):
  if node: 
    postorder(node.left)
    postorder(node.right)
    print(node.value, end = "")


#using recursion and dfs to find the sum of all the nodes 
def sum(root):
  if root is None: 
    return 0 
  
  return root.val + sum(root.left) +sum(root.right)

#finding the number of nodes
def count(root):
  if root is None: 
    return 0 
  
  return 1+ count(root.left) + count(root.right)

#finding the largest node
def max_value(root): 
  if root is None: 
    return 0
  
  left_max = max_value(root.left)
  right_max = max_value(root.right)

  return max(root.val, left_max, right_max)

##finding the height of a binary tree
def height(root):
  if root is None: 
    return 0 
  
  left_height = height(root.left)
  right_height = height(root.right)

  return 1 + max(left_height, right_height)

##finding the minimum depth
##min depth is the number of nodes leading to the leaf
def min_depth(root: TreeNode) -> int:
    if not root:
        return 0
    
    # If no left child
    if not root.left:
        return 1 + min_depth(root.right)
    
    # If no right child
    if not root.right:
        return 1 + min_depth(root.left)
    
    return 1 + min(min_depth(root.left), min_depth(root.right))

#checking to see if a binary tree is balanced 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBalanced(root):
    def dfs(node):
        if node is None:
            return 0

        left = dfs(node.left)
        if left == -1:
            return -1

        right = dfs(node.right)
        if right == -1:
            return -1

        if abs(left - right) > 1:
            return -1

        return 1 + max(left, right)

    return dfs(root) != -1



#diamater of a binary tree 
#diameter of a tree is the length of the longest path between any two nodes in the tree. 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution: 
  def __init__(self): 
    self.max_diameter = 0 
  def diameterOfBinaryTree(self,root):    
    def dfs(node):
      if not node: 
        return 0 
    
      left_height = dfs(node.left)
      right_height = dfs(node.right)

      self.max_diameter = max(self.max_diameter, right_height+left_height)

      return 1+ max(left_height,right_height)
    dfs(root)
    return self.max_diameter

#least common ancestor 
def dfs(node):
    if not node:
        return None

    if node == p or node == q:
        return node

    left = dfs(node.left)
    right = dfs(node.right)

    if left and right:
        return node

    return left if left else right

#cycle detection 

#topological sort

##BREADTH-FIRST TRAVERSAL 
def bfs(root):
    if not root:
        return []

    queue = deque([root])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node.val)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return result


#this involves visiting nodes level by level
#Level order output
def levelorder():
  queue= deque([root])
  result = []

  while queue: 
    level_size = len(queue)
    level= []
    for _ in range(level):
      node = queue.popleft()
      level.append(node.val)

      if node.left: 
        queue.append(node.left)
      if node.right: 
        queue.append(node.right)
          
      result.append(level)

  return result
#minimum depth of a binary tree
def minDepth(root):
  if not root: 
    return 0 
  queue = deque([(root,1)])

  while queue: 
    node, depth = queue.popleft() 

    if not node.left and not node.right:
       return depth 
    
    if node.left: 
       queue.append((node.left, depth+1))
    
    if node.right: 
       queue.append((node.right, depth+1))




#Right-side view
def rightSideView(root):
   if not root: 
      return []
   result = []

   queue = deque([root])

   while queue:
      level_size = len(queue)

      for i in range(level_size):
         node = queue.popleft() 

         if node.left:
            queue.append(node.left)
         if node.right: 
            queue.append(node.right)


         if i==level_size-1:
            result.append(node.val)
         return result
#left-side view of a tree 
#basically the same thing but i ==0 



#Maximum per level
def max_per_level(root):
  queue =  deque([root])
  max = []
  while queue:
    level_max = 0
    level_size = len(queue)

    for _ in range(level_size):
      node = queue.popleft()
      level_max = max(level_max, node.val)

      if node.left:
         queue.append(node.left)
      if node.right: 
         queue.append(node.right)

    max.append(level_max)
  return max

#zizag 
def zigzagLevelOrder(root):
  if not root: 
     return []
  result =[]
  queue = deque([root])
  left_to_right = True 

  while queue:
     level_size = len(queue)
     level = deque() 

     for _ in range(level_size):
        node = queue.popleft()
     if left_to_right:
        level.append(node.val)
     else: 
        level.appendleft(node.val)

     if node.left:
        queue.append(node.left)
     if node.right; 
        queue.append(node.right)
  result.append(list(level))
  left_to_right = not left_to_right

  return result 
from collections import deque

def connectNextRight(root):
    if not root:
        return None
    
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        prev_node = None
        
        for _ in range(level_size):
            node = queue.popleft()
            
            # connect previous node's next to current node
            if prev_node:
                prev_node.next = node
            prev_node = node
            
            # add children
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # last node in level points to None automatically
        prev_node.next = None
    
    return root


#check if tree is complete 



#