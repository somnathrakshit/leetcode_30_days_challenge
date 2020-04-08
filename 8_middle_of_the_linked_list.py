# Title: Middle of the Linked List
# URL: https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        ptr = head
        while (ptr and ptr.next):
            head = head.next
            ptr = ptr.next.next
        return head
