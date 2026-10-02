"""
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""

"""
I use two pointers to traverse the two sorted linked lists and a dummy node to build the merged list.

While both lists still have nodes, I compare their current values and attach the smaller node to the result. Then I move forward in the list from which the node was taken, and also move the current pointer forward.

When one list becomes empty, I can directly attach the remaining part of the other list because it is already sorted.

The time complexity is **O(m + n)**, where `m` and `n` are the lengths of the two lists, because each node is visited at most once.

The space complexity is **O(1)** because I reuse the existing nodes and only use a few extra pointers.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: ListNode | None, list2: ListNode | None
    ) -> ListNode | None:

        dummy_head = ListNode(0)
        curr = dummy_head

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next

        if list1:
            curr.next = list1
        else:
            curr.next = list2

        return dummy_head.next
