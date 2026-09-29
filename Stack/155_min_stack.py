"""
155. Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int value) pushes the element value onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

Example 1:
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]]
Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
"""

"""
I use an auxiliary stack to track the current minimum, so all operations can be done in O(1) time.

The main stack stores all values normally, while the auxiliary `min_stack` stores the minimum values.

When I push a new value, I always add it to the main stack. If it is smaller than or equal to the current minimum, I also push it to `min_stack`.

When I pop a value, if it is equal to the top of `min_stack`, I pop from `min_stack` as well.

For `top()`, I return the top of the main stack. For `getMin()`, I directly return the top of `min_stack`.

All four operations — `push`, `pop`, `top`, and `getMin` — take O(1) time.

The space complexity is O(n), because the auxiliary stack may store up to n elements.
"""


class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value: int) -> None:
        self.stack.append(value)

        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self) -> None:
        pop_element = self.stack.pop()

        if pop_element == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
