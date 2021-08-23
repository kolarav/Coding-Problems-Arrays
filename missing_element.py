from typing import List


class Solution:
    def missing_number(self, nums: List[int]) -> int:
        n = len(nums)
        s = int((n*(n + 1))/2)
        return (s - sum(nums))


solution = Solution()
print(solution.missing_number([1, 2, 7, 3, 8, 4, 6, 0]))
