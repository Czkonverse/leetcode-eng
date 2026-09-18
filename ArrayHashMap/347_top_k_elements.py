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

    # quick select - similar to quick sort
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        record = defaultdict(int)

        for num in nums:
            record[num] += 1

        unique = list(record.keys())

        pivot_idx = random.randint(0, len(nums) - 1)

if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    k = 2

    solution = Solution()

    res = solution.topKFrequent(nums, k)