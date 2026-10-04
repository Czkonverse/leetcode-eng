class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_linked_list(values: list[int]) -> ListNode | None:
    dummy = ListNode(0)
    curr = dummy

    for value in values:
        curr.next = ListNode(value)
        curr = curr.next

    return dummy.next


def print_linked_list(head: ListNode | None) -> None:
    values = []

    curr = head
    while curr:
        values.append(str(curr.val))
        curr = curr.next

    print(" -> ".join(values) + " -> None")


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev

            prev = curr
            curr = next_node

        return prev


# test
root = [1, 2, 3, 4, 5]

head = build_linked_list(root)

print("Before:")
print_linked_list(head)

solution = Solution()
new_head = solution.reverseList(head)

print("After:")
print_linked_list(new_head)
