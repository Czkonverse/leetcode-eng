"""
206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        self.stack = []

        while head:
            self.stack.append(head.val)
            head = head.next

        dummy_head = ListNode(0)
        pointer = dummy_head
        while len(self.stack) != 0:
            val = self.stack.pop()
            new_node = ListNode(val)
            pointer.next = new_node
            pointer = pointer.next

        return dummy_head.next
