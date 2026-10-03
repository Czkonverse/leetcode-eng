"""
143. Reorder List

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
My first approach is to store all the nodes in an array.

Then I use two pointers, one from the beginning and one from the end, and reconnect the nodes in the required order: first, last, second, second-last, and so on.

This approach is straightforward and runs in O(n) time because I traverse the list once to store the nodes and once more to reorder them. 
However, it requires O(n) extra space for the array.
"""


class Solution:
    def reorderList(self, head: ListNode | None) -> None:

        if not head:
            return

        nodes = []

        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        left = 0
        right = len(nodes) - 1
        while left < right:
            nodes[left].next = nodes[right]
            left += 1

            if left == right:
                break

            nodes[right].next = nodes[left]
            right -= 1

        nodes[left].next = None


"""
To optimize the space complexity, I noticed that I do not actually need to store all the nodes. I only need the first half in forward order and the second half in reverse order.

So I improve the solution in three steps.

First, I use slow and fast pointers to find the middle of the linked list and split it into two halves.

Second, I reverse the second half of the list in place.

Finally, I merge the two halves alternately. I save the next nodes before changing the pointers, then connect one node from the first half and one node from the reversed second half.

The optimized solution still takes O(n) time, because finding the middle, reversing the second half, and merging the lists are all linear operations.
The space complexity is reduced from O(n) to O(1), because I only use a constant number of pointers.
"""


class Solution:
    def reorderList(self, head: ListNode | None) -> None:

        if not head or not head.next:
            return

        # 1 find the middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # split the linked-list
        second = slow.next
        slow.next = None

        # 2 reverse the second half
        prev = None
        curr = second

        while curr:
            next_node = curr.next

            curr.next = prev

            prev = curr
            curr = next_node

        second = prev

        # 3 merge two halves
        first = head

        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next
