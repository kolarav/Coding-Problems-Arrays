# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# Input: nums = [1, 3, 5, 6], target = 5
# Output: 2

# Input: nums = [1, 3, 5, 6], target = 2
# Output: 1

# Input: nums = [1, 3, 5, 6], target = 7
# Output: 4
from typing import List


#  Using binary search in O(log n) time and O(1) space
class Solution:
    def search(self, nums, target, low, high):

        mid = (low + high)//2
        if(mid >= high or target == nums[mid]):
            return mid
        elif target > nums[mid]:
            return self.search(nums, target, mid+1, high)
        else:
            return self.search(nums, target, low, mid)

    def search_insert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)
        return self.search(nums, target, low, high)


solution = Solution()
nums = [1, 3, 5, 6]
target = 2
index = solution.search_insert(nums, target)
print(index)
