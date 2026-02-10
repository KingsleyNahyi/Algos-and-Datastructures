#double linked lists essentially have two pointers one pointing forward and backward 
#they are meant to have more structure but the trade off is memory because they are expensive. 
#this is its creation here we see it is pointing forward and backwards
class Node: 
  def __init__(self,data):
    self.data = data 
    self.prev = None
    self.next = None 

class DoublyLinkedList: 
  def __init__(self):
    self.head = None
    self.tail = None 

#inserting at the head
  def insert_at_head(self,data):
    new_node = Node(data)
  
    if self.head is None: 
      self.head = self.tail = new_node
      return 
  
    new_node.next = self.head
    self.head.prev = new_node
    self.head = new_node 


  #inserting at the tail 
  def insert_at_tail(self, data):
    new_node = Node(data)

    if self.tail is None: 
      self.head = self.tail = new_node 
      return 
  
    new_node.prev = self.tail 
    self.tail.next = new_node 
    self.tail = new_node


  #inserting at the middle 
  def insert_after(self, node,data):
    if node is None: 
      return 

    new_node = Node(data)

    new_node.prev = node 
    new_node.next = node.next

    if node.next is not None: 
      node.next.prev = new_node
    else: 
      self.tail = new_node 
    
    node.next = new_node 

#deleting the head 
  def delete_head(self):
    if self.head is None: 
      return 
  
    #if it's just one node
    if self.head == self.tail: 
      self.head = self.tail = None
    
    #Normal case 
    #reassing head to be what head's next value is and make sure head's previous is none
    self.head = self.head.next 
    self.head.prev = None 

#deleting the tail 
  def delete_tail(self):
    if self.tail is None: 
      return 
    
    if self.head ==self.tail: 
      self.head = self.tail = None 
      return 
  
    self.tail = self.tail.prev 
    self.tail.next = None

#deleting a middle 
  def delete(self,node):
    if node == self.head: 
      self.delete_head() 
      return 
    
    if node== self.tail: 
      self.delete_tail()
      return 
    
    node.prev.next = node.next 
    node.next.prev = node.prev 

#traversal of a linked list 
def traverse_forward(self):
  curr = self.head 
  while curr: 
    curr = curr.next

def traverse_backword(self):
  curr = self.tail 
  while curr: 
    curr = curr.prev 


#reversal algorithm for double linked list 
def reverse(self):
    curr = self.head
    while curr:
        # swap pointers
        curr.prev, curr.next = curr.next, curr.prev
        # move to the next node (which is prev after swapping)
        curr = curr.prev
    # swap head and tail
    self.head, self.tail = self.tail, self.head
