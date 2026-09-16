"""Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers index1 and index2, each incremented by one, as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
"""

"""
My first idea is to use a hash map to store each number and its index.

I can iterate through the array, and for each number, calculate its complement as `target - number`. Then I check whether the complement already exists in the hash map.

This approach would take O(n) time, but it also requires O(n) extra space.

However, this problem requires constant extra space, so I need another approach.

Since the array is already sorted, I can use two pointers. I put one pointer at the beginning of the array and the other pointer at the end.

Then I calculate the current sum as `numbers[left] + numbers[right]`.

If the current sum is greater than the target, the sum is too large. Because the array is sorted, moving the right pointer one step to the left gives me a smaller number, so I decrease the right pointer.

If the current sum is smaller than the target, I need a larger sum. So I move the left pointer one step to the right, which gives me a larger number.

If the current sum equals the target, I return the two indices. Since the problem uses 1-based indexing, I add one to both indices before returning them.

The time complexity is O(n) because each pointer moves at most n times, and the space complexity is O(1).
"""
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:

        left_p = 0
        right_p = len(numbers) - 1
        while left_p < right_p:
            temp_num = numbers[left_p] + numbers[right_p]
            if target < temp_num:
                right_p -= 1
            elif target > temp_num:
                left_p += 1
            else:
                return [left_p+1, right_p + 1]
            
