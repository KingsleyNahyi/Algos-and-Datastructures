class ListNode: 
  def __init__(self, value):
    self.value = value 
    self.next = None

firstnode = ListNode(10)
secondnode = ListNode(20)

firstnode.next = secondnode
secondnode.next = None 
head = firstnode

#traversing a singly linked list 
curr = head 
while curr: 
  print(curr.value) 
  curr = curr.next 

#inserting node at head (O(1))
new_node = ListNode(2)
new_node.next = head 
head = new_node 

#inserting at the tail (O(n))
curr = head 
while curr.next: 
  curr = curr.next

curr.next = new_node

#deleting the head 
head = head.next 
#this would move head from it's current to the next node and drop the original head it is also O(1)

#deleting a node by VALUE 
while curr.next and curr.next.value!= new_node: 
  curr = curr.next 

if curr.next: 
  curr.next = curr.next.next


#infind the middle of a linked list 
slow = head
fast = head
#slow is moving half the speed of fast 
#fast is there to ensure fast exists 
#fast.next is there because it is a possibility that the next can be just one item which is the haeder.
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

print(slow.value)  # middle


#reversing a singly linked list 
prev = None
curr = head
while curr:
    next_node = curr.next   # temporarily store next node
    curr.next = prev        # reverse the link
    prev = curr             # move prev forward
    curr = next_node        # move curr forward
