"""
215. Kth Largest Element in an Array

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
"""

"""
### 1. Explain the approach

To solve this problem without sorting the entire array, I would use **Quickselect**.

The key idea is that we don't need to sort the whole array. We only need to find the element at a specific index.

Since we're looking for the kth largest element, I first convert `k` into a zero-based index:

`target = len(nums) - k`

### 2. Explain the partition

Next, I use a randomized pivot to partition the array.

I randomly select a pivot and move it to the end of the current search range.

Then, I use a pointer called `store_idx` to track where the next smaller element should go.

I iterate through the array. Whenever I find an element smaller than the pivot, I swap it with the element at `store_idx` and increment `store_idx`.

After the loop, I swap the pivot with the element at `store_idx`.

Now, the pivot is in its final sorted position.

### 3. Explain Quickselect

I compare the pivot's final index with the target index.

- If they are equal, I return the pivot.
- If the pivot index is smaller than the target, I search the right side.
- Otherwise, I search the left side.

I repeat this process until I find the target element.

### 4. Complexity analysis

The expected time complexity is **O(n)** because we use a randomized pivot and only search one side after each partition.

In the worst case, the time complexity can be **O(n²)**.

The extra space complexity is **O(1)** because the algorithm modifies the array in place and doesn't require any additional arrays.
"""
import random


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:

        left = 0
        right = len(nums) - 1

        target = len(nums) - k

        while left <= right:
            pivot_idx = random.randint(left, right)
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]

            store_idx = left
            pivot = nums[right]
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_idx], nums[i] = nums[i], nums[store_idx]

                    store_idx += 1

            nums[right], nums[store_idx] = nums[store_idx], nums[right]

            pivot_idx = store_idx

            if pivot_idx == target:
                return nums[pivot_idx]
            elif pivot_idx < target:
                left = pivot_idx + 1
            else:
                right = pivot_idx - 1

        return -1


"""
[left, lt)       < pivot
[lt, i)          == pivot
(gt, right]      > pivot
"""

import random

"""
### 1. Explain the approach

I would use **Randomized Quickselect with three-way partitioning**.

The idea is to find the kth largest element without sorting the entire array.

First, I convert `k` into a zero-based target index:

`target = len(nums) - k`

Then, I randomly select a pivot from the current search range.

### 2. Explain three-way partitioning

Instead of dividing the array into two parts, I divide it into three parts:

- Elements smaller than the pivot.
- Elements equal to the pivot.
- Elements greater than the pivot.

To do this, I use three pointers: `lt`, `i`, and `gt`.

`lt` marks the boundary of the smaller elements, `i` is the current scanning index, and `gt` marks the boundary of the greater elements.

I initialize `lt` and `i` to `left`, and `gt` to `right`.

### 3. Explain the three cases

While `i <= gt`, there are three possible cases.

**First**, if `nums[i]` is smaller than the pivot, I swap it with `nums[lt]`, then increment both `lt` and `i`.

**Second**, if `nums[i]` is greater than the pivot, I swap it with `nums[gt]` and decrement `gt`.

Notice that I don't increment `i` in this case, because the element swapped from the right hasn't been checked yet.

**Finally**, if `nums[i]` equals the pivot, I simply increment `i`.

### 4. Explain how to find the answer

After partitioning, all elements equal to the pivot are between indices `lt` and `gt`.

I compare the target index with this range.

- If the target is smaller than `lt`, I continue searching the left side.
- If the target is greater than `gt`, I continue searching the right side.
- Otherwise, the target falls within the equal-to-pivot region, so I return the pivot directly.

### 5. Complexity analysis

The expected time complexity is **O(n)**, thanks to the randomized pivot and the fact that we only search one side after partitioning.

The worst-case time complexity is still **O(n²)**.

The extra space complexity is **O(1)** because all operations are performed in place.

Three-way partitioning is especially useful when the array contains many duplicate elements, because we can process all elements equal to the pivot in a single partition.
"""


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        target = len(nums) - k

        left = 0
        right = len(nums) - 1

        while left <= right:
            pivot = nums[random.randint(left, right)]

            # [left, lt)       < pivot
            # [lt, i)          == pivot
            # (gt, right]      > pivot
            lt = left
            i = left
            gt = right

            while i <= gt:
                if nums[i] < pivot:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1

                elif nums[i] > pivot:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1

                else:
                    i += 1

            if target < lt:
                right = lt - 1

            elif target > gt:
                left = gt + 1

            else:
                return pivot

        return -1
