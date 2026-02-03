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

##recursive transversing 
def transverse_recursively(head):
    if not head: 
      print("none")
      return None 
    print(head.val, end = "->")
    transverse_recursively(head.next)







##seraching for a value 
def search_linked_list(head, key):
    curr = head
    while curr:
        if curr.data == key:
            return True   # key found
        curr = curr.next
    return False  # key not found

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
    prev = curr              # move prev forward
    curr = next_node        # move curr forward
  
#reversing recursively 
def reverse_list_recursive(head):
    if not head or not head.next:    
        return head 
    new_head = reverse_list_recursive(head.next)
    head.next.next = head 
    head.next = None 

    return new_head 




#checking for loops 
def has_cycle(head):
  slow = head 
  fast = head 
  while fast and fast.next: 
    slow = slow.next 
    fast = fast.next.next 
    if slow ==fast: 
      return True 
  return False
  #checking where the cycle began 
def cycle_begin(head):
  slow = head 
  while slow!=fast: 
    slow = slow.next 
    fast = fast.next 
  return slow 



##merging two linked lists 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def mergeTwoLists(l1, l2):
    # Dummy node to simplify handling head
    dummy = ListNode()
    tail = dummy

    # Traverse both lists
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    # Attach remaining nodes
    if l1:
        tail.next = l1
    else:
        tail.next = l2

    return dummy.next

##checking if linked list is a palindrome 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head):
    if not head or not head.next:
        return True

    # Step 1: Find middle
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse second half
    prev = None
    curr = slow
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    # Now 'prev' is head of reversed second half

    # Step 3: Compare halves
    left, right = head, prev
    while right:  # only need to check second half
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    return True

#swapping pairs 
def swapPairs(head):
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    while prev.next and prev.next.next:
        first = prev.next
        second = first.next

        # swap
        prev.next = second
        first.next = second.next
        second.next = first

        # move prev forward
        prev = first

    return dummy.next


#reordering the list by reversing using group
def reverseKGroup(head, k):
    dummy = ListNode(0)
    dummy.next = head
    prev_group = dummy

    while True:
        # 1. Find kth node
        kth = prev_group
        for _ in range(k):
            kth = kth.next
            if not kth:
                return dummy.next

        group_next = kth.next

        # 2. Reverse group
        prev = group_next
        curr = prev_group.next
        while curr != group_next:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # 3. Reconnect
        tmp = prev_group.next   # original head of group (tail after reverse)
        prev_group.next = kth
        prev_group = tmp

        #reordering a list
        #this keeps switching the front and the back
def reorderList(head):
    if not head or not head.next:
        return

    # 1. Find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # 2. Reverse second half
    second = slow.next
    slow.next = None

    prev = None
    curr = second
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    # 3. Merge
    first = head
    second = prev

    while second:
        temp1 = first.next
        temp2 = second.next

        first.next = second
        second.next = temp1

        first = temp1
        second = temp2

#partitioning 
def partition(head, x):
    less_dummy = ListNode(0)
    greater_dummy = ListNode(0)

    less = less_dummy
    greater = greater_dummy
    curr = head

    while curr:
        if curr.val < x:
            less.next = curr
            less = less.next
        else:
            greater.next = curr
            greater = greater.next
        curr = curr.next

    greater.next = None
    less.next = greater_dummy.next

    return less_dummy.next

def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head
    slow = fast = dummy

    # Move fast n steps ahead
    for _ in range(n):
        fast = fast.next

    # Move both until fast reaches the end
    while fast.next:
        slow = slow.next
        fast = fast.next

    # Remove the N-th node
    slow.next = slow.next.next

    return dummy.next

#removing at position 
def removeAtPosition(head, pos):
    dummy = ListNode(0)
    dummy.next = head
    current = dummy

    for _ in range(pos - 1):
        if current.next is None:
            return head  # position out of bounds
        current = current.next

    # Remove the node
    if current.next:
        current.next = current.next.next

    return dummy.next

#sorting linked lists 
def merge(l1, l2):
    dummy = ListNode(0)
    tail = dummy
    
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    
    tail.next = l1 if l1 else l2
    return dummy.next
def sortList(head):
    if not head or not head.next:
        return head
    
    mid = getMid(head)
    left = sortList(head)
    right = sortList(mid)
    
    return merge(left, right)
def sortList(head):
    if not head or not head.next:
        return head
    
    mid = getMid(head)
    left = sortList(head)
    right = sortList(mid)
    
    return merge(left, right