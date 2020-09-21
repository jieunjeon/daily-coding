"""
160. Intersection of Two Linked Lists
https://leetcode.com/problems/intersection-of-two-linked-lists/

Write a program to find the node at which the intersection of two singly linked lists begins.

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA = self._length(headA)
        lenB = self._length(headB)
        currA = headA
        currB = headB

        if lenA > lenB:
            for _ in range(lenA - lenB):
                currA = currA.next
        else:
            for _ in range(lenB - lenA):
                currB = currB.next

        while currA != currB:
            currA = currA.next
            currB = currB.next

        return currA

    def _length(self, n):
        len = 0
        curr = n
        while curr:
            curr = curr.next
            len += 1
        return len