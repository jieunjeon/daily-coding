"""
https://leetcode.com/problems/merge-k-sorted-lists/
23. Merge k Sorted Lists


You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKListsBruteForce(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        arr = []
	    for node in lists:
	        while node:
	            arr.append(node.val)
	            node = node.next
	    head = root = None
	    for val in sorted(arr):
	        if not root:
	            head = root = ListNode(val)
	        else:
	            root.next = ListNode(val)
	            root = root.next
	    return head

    def mergeKListsImproved(self, lists):
	    """
	    :type lists: List[ListNode]
	    :rtype: ListNode
	    """
	    def check_if_none(list):
	        for i in range(len(list)):
	            if (list[i] is not None):
	                return True
	        return False
	    
	    head = current = ListNode(-1)
	    while (check_if_none(lists)):
	        index = -1
	        curr_min = float("inf")
	        for i, nlist in enumerate(lists):
	            if (nlist is not None and nlist.val < curr_min):
	                index = i
	                curr_min = nlist.val
	        lists[index] = lists[index].next
	        current.next = ListNode(curr_min)
	        current = current.next
	    return head.next

    def mergeKListsPriorityQueue(self, lists):
	    """
	    :type lists: List[ListNode]
	    :rtype: ListNode
	    """
        head = point = ListNode(0)
		q = PriorityQueue()
		for i, l in enumerate(lists):
		    if l:
		        q.put((l.val, i, l))
	
		while not q.empty():
		    val, i, node = q.get()
		    print("asdf", val, i)
		    point.next = ListNode(val)
		    point = point.next
		    node = node.next
		    if node:
		        q.put((node.val, i, node))
		        print("node", node)

		return head.next


        