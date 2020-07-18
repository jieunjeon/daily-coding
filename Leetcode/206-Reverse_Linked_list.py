"""
https://leetcode.com/problems/reverse-linked-list/
206. Reverse Linked List
Easy

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

Time Complexity: O(n) while n is the number of the nodes in the given list
Space Complexity: O(1)

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        prev = None

        while curr != None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev
        