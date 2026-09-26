"""
128. Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.


Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Example 3:
Input: nums = [1,0,1,2]
Output: 3
"""

"""
Approach 1: Sort and Scan

My first idea is to sort the array and then scan it from left to right.

If the current number is the same as the previous one, I skip it because duplicates do not increase the sequence length.

If the current number is exactly one greater than the previous number, I increase the current sequence length. Otherwise, I reset the length to 1.

The time complexity is O(n log n) because sorting takes O(n log n), so this approach does not satisfy the required O(n) time complexity.
"""
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()

        max_len = 1
        len_succ = 1

        for i in range(1, len(nums)):
            # duplicate
            if nums[i] == nums[i - 1]:
                continue

            if nums[i] == nums[i - 1] + 1:
                len_succ += 1
            else:
                len_succ = 1

            max_len = max(max_len, len_succ)
            
        return max_len

"""
Approach 2: Hash Set

To achieve O(n) time, I use a hash set, which gives O(1) average lookup time.

For each number, I first check whether num - 1 exists in the set.

If it does, then num is not the start of a sequence, so I skip it.

If num - 1 does not exist, then num is the start of a sequence. I keep checking num + 1, num + 2, and so on until the sequence ends, while counting its length.

Finally, I keep track of the maximum sequence length.

The time complexity is O(n) on average. Although there is a while loop inside the for loop, each number is visited at most once as part of a consecutive sequence.

The space complexity is O(n) for the hash set.
"""
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        nums_set = set(nums)

        max_len = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                current_num = num
                current_len = 1

                while current_num + 1 in nums_set:
                    current_num += 1
                    current_len += 1

                max_len = max(max_len, current_len)

        return max_len


        
# nums = [100,4,200,1,3,2]
# solution = Solution()
# max_len = solution.longestConsecutive(nums)
# print(max_len)