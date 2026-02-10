#introduction to trees in general 
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

def count(root):
  if root is None: 
    return 0 
  
  return 1+ count(root.left) + count(root.right)

def max_value(root): 
  if root is None: 
    return 0
  
  left_max = max_value(root.left)
  right_max = max_value(root.right)

  return max(root.val, left_max, right_max)

def height(root):
  if root is None: 
    return 0 
  
  left_height = height(root.left)
  right_height = height(root.right)

  return 1 + max(left_height, right_height)



##BREADTH-FIRST TRAVERSAL 
#this involves visiting nodes level by level