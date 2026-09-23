"""
347 Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Example 3:
Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
Output: [1,2]

"""

"""
### First approach: Hash Map + Sorting

My first idea is to use a hash map and sorting.

First, I iterate through the array and use a hash map to count the frequency of each number.

Then, I sort all unique numbers by their frequencies in descending order.

After sorting, I simply take the first `k` elements as the result.

Let `n` be the number of elements in the input array, and let `m` be the number of unique elements.

Counting the frequencies takes `O(n)` time, and sorting the unique elements takes `O(m log m)` time.

Therefore, the total time complexity is `O(n + m log m)`, which is `O(n log n)` in the worst case.

The space complexity is `O(m)`.

"""

from collections import defaultdict
import random

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        record = defaultdict(int)

        for num in nums:
            record[num] += 1

        sorted_record = dict(sorted(record.items(), key=lambda item: item[1], reverse=True))

        res = []
        count = 0
        for k, v in sorted_record.items():
            if count < k:
                res.append(k)

            return res
    """
    ### Second approach: Quickselect

    A better approach is to use Quickselect.

    The key idea is that we do not need to fully sort the array. We only need to find the boundary of the top `k` frequent elements.

    First, I count the frequencies and create an array of unique numbers.

    Then, I apply Quickselect to this array, comparing elements by their frequencies instead of their values.

    Since I partition by frequency in ascending order, the target index is:

    `len(unique) - k`

    For each partition, I randomly choose a pivot. After partitioning, elements with smaller frequencies are on the left, and elements with greater or equal frequencies are on the right. The two sides do not need to be internally sorted.

    Then, I compare the pivot index with the target index and continue searching only on the side that contains the target.

    Once the pivot reaches the target index, I return:

    `unique[target:]`

    The average time complexity is `O(n)`, while the worst case is `O(n²)`.

    The space complexity is `O(m)`.
    """
    # quick select - similar to quick sort
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        record = defaultdict(int)

        for num in nums:
            record[num] += 1

        unique = list(record.keys())

        left = 0
        right = len(unique) - 1

        target = len(unique) - k

        # partition
        store_idx = left

        while left <= right:
            # randomly choose pivot
            pivot_idx = random.randint(left, right)
            pivot = unique[pivot_idx]

            # move pivot to the end
            unique[pivot_idx], unique[right] = unique[right], unique[pivot_idx]

            for i in range(left, right):

                if record[unique[i]] < record[pivot]:
                    unique[store_idx], unique[i] = unique[i], unique[store_idx]

                    store_idx += 1

            # move pivot to its final position
            unique[store_idx], unique[right] = unique[right], unique[store_idx]

            pivot_idx = store_idx

            if pivot_idx < target:
                left = pivot_idx + 1
            elif pivot_idx > target:
                right = pivot_idx - 1
            else:
                break

        return unique[target:]


if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    k = 2

    solution = Solution()

    res = solution.topKFrequent(nums, k)