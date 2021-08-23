# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Input : nums = [2, 2, 1, 1, 1, 2, 2]  Output: 2


from typing import List


#  time : O(nlog n) space : O(1) if sort the same list  O(n) if we need to copy the list,
#  For this problem as the majority element will have count more than half of the size of list
# so no matter what  we can find that element at the middle of the list if we sort the list
class Solution:
    def majority_element(self, nums):
        nums.sort()
        return nums[len(nums)//2]

solution = Solution()
print(solution.majority_element([1, 1, 1, 2, 2, 2, 2]))




#  time : O(n) space : O(n)
# class Solution:
#     def majority_element(self, nums: List[int]) -> int:
#         count = {}
#         for num in nums:
#             if num in count:
#                 count[num] = count[num] + 1

#             else:
#                 count[num] = 1
#             # for this problem statement we can do this as majority_element will have more than half count of the length of list
#             if count[num] > len(nums)/2:
#                 return num
        # for all cases where count is not defined as this problem
        # return(max(count, key=count.get))


# time : O(n) space : O(1)
# class Solution:
#     def majority_element(self, nums):
#         count = 0
#         candidate = None

#         for num in nums:
#             if count == 0:
#                 candidate = num
#             count += (1 if num == candidate else -1)
#         return candidate



