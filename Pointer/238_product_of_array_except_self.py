"""
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 
Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""

"""
Approach 1: Brute Force

My first idea is to use brute force.

For each position, I iterate through the whole array and multiply all the elements except the current one.

This is straightforward, but it repeats a lot of multiplication.

The time complexity is O(n²) because for each of the n elements, I scan the array again.

The space complexity is O(n) for the result array.
"""
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans = []

        for i in range(len(nums)):

            product = 1
            for j in range(len(nums)):
                if i == j:
                    continue

                product = product * nums[j]
            ans.append(product)

        return ans

"""
Approach 2: Prefix and Suffix Arrays

We can avoid repeated calculations by precomputing the product on both sides of each element.

previous_product[i] stores the product of all elements before index i.

after_product[i] stores the product of all elements after index i.

Then the answer for each position is:

previous_product[i] * after_product[i]

The time complexity is O(n) because we only scan the array a few times.

The extra space complexity is O(n) because we use two additional arrays for prefix and suffix products.
"""
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        previous_product = []
        for i in range(len(nums)):
            if i == 0:
                previous_product.append(1)
            else:
                product = previous_product[i - 1] * nums[i - 1]
                previous_product.append(product)

        after_product = [0] * len(nums)
        for j in range(len(nums) - 1, -1, -1):
            if j == len(nums) - 1:
                after_product[j] = 1
            else:
                product = after_product[j + 1] * nums[j + 1]
                after_product[j] = product

        ans = []
        for i in range(len(nums)):
            product = previous_product[i] * after_product[i]
            ans.append(product)

        return ans

"""
Approach 3: Optimized Prefix and Suffix

We can further optimize the space.

First, I use the result array itself to store the prefix products.

Then I scan the array from right to left and maintain a suffix variable.

At each position, I multiply the stored prefix product by the current suffix product.

This gives the product of all elements except the current one.

The time complexity is O(n) because we make two linear passes.

The extra space complexity is O(1) if we don't count the output array, because we only use the prefix and suffix variables.

So this is the optimal solution.
"""
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)

        ans = [1] * n

        # prefix products
        prefix = 1
        for i in range(n):
            ans[i] = prefix
            prefix *= nums[i]

        # suffix products
        suffix = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]

        return ans
    
if __name__ == "__main__":
    nums = [1,2,3,4]

    solution = Solution()

    res = solution.productExceptSelf(nums)
    print(res)