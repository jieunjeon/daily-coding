"""
Given a linked list, swap the position of the 1st and 2nd node, then swap the position of the 3rd and 4th node etc.
"""

# swap the values of each node instead, which makes the problem substantially easier. Have a while loop that keeps track of a current node variable, and then swap its value with the next node's value, and then set current to node two steps away.
"""
The time complexity is O(n) for processing the whole list, and the space complexity is O(1).
"""
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def __repr__(self):
    return f"{self.value}, ({self.next.__repr__()})"

def swap_every_two(llist):
  head = llist

  curr = head
  while curr is not None and curr.next is not None:
    curr.value, curr.next.value = curr.next.value, curr.value
    curr = curr.next.next

  return head

llist = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(swap_every_two(llist))
# 2, (1, (4, (3, (5, (None)))))