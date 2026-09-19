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

        pivot_idx = random.randint(0, len(unique) - 1)
        temp_num = unique[-1]
        unique[-1] = unique[pivot_idx]
        unique[pivot_idx] = temp_num

        temp_nums = [unique[pivot_idx]]
        for i in range(0, len(unique) - 2):
            if record[unique[i]] < record[unique[pivot_idx]]:
                temp_nums = [record[unique[i]]] + temp_nums
            else:
                temp_nums = temp_nums + [record[unique[i]]]

        if pivot_idx > k-1:
            pass
        elif pivot_idx < k-1:
            pass
        else:
            pass


if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    k = 2

    solution = Solution()

    res = solution.topKFrequent(nums, k)