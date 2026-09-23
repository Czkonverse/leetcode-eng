"""
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

"""
mistakes: 
How to traverse the linked list ? 
Why we need a dummy head, instead of store the number in the first node of linked list ?
How to check whether node contains value or not ?
How to move the reference to the next node in the same linked list ?

dummy 是一个变量，curr 是一个变量，它们可以引用 ListNode 对象。

变量          对象

dummy ─────┐
           ↓
         ListNode(0)
           ↑
curr ──────┘

curr.next = newNode
curr = newNode

把curr当前引用的节点对象的next，指向newNode，相当于把newNode接到了curr当前引用的对象节点的后面；
然后，curr去引用新的newNode，相当于curr指向了newNode；
"""

"""
I use a dummy node to simplify building the result linked list.

Then I traverse both linked lists at the same time. At each position, I add the two values together with the carry from the previous position.

I use modulo 10 to get the current digit and integer division by 10 to calculate the new carry. 
Then I append the current digit as a new node to the result list.

The loop continues until both lists are finished and there is no remaining carry.

The time complexity is O(max(m, n)), and the space complexity is O(max(m, n)) for the result list.

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        curr = dummy

        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            quotient = (val1 + val2 + carry) // 10
            remainder = (val1 + val2 + carry) % 10
            carry = quotient

            new_node = ListNode(remainder)
            curr.next = new_node
            curr = new_node

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
