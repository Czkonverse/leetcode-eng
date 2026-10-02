"""
19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.


Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
My first approach is to store each node in a hash map using its index.

After traversing the list, I know the total number of nodes. The index of the node to remove is length - n. If it is the head node, I simply return head.next. Otherwise, I connect the previous node directly to the node after the one being removed.

This approach takes O(L) time because I traverse the list once, and O(L) extra space because I store all nodes in the hash map.
"""


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        records = {}

        idx = 0

        curr = head
        while curr:
            records[idx] = curr
            idx += 1

            curr = curr.next

        delet_idx = idx - n
        if delet_idx == 0:
            return head.next
        else:
            front_node = records[delet_idx - 1]
            delet_node = records[delet_idx]
            front_node.next = delet_node.next

        return head


"""
A better approach is to use two pointers with a dummy node.

I move the fast pointer n steps ahead first. Then I move both slow and fast pointers together until fast reaches the last node. At that point, slow is right before the node I need to remove.

I remove it with:

slow.next = slow.next.next

The dummy node also makes removing the head node easy, without requiring a special case.

This optimized approach takes O(L) time because the list is traversed only a constant number of times, and O(1) extra space because I only use a few pointers.
"""


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:

        dummy = ListNode(0, head)

        slow = dummy
        fast = dummy

        for _ in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next
