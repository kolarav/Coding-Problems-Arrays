from typing import List

# Time : worst case ->  O(N^2) best case O(N) Space : O(N)
# class Solution:
#     def smaller_than_current(self, nums: List[int]) -> List[int]:
#         smaller = []
#         scount = {}

#         for num in nums:
#             if num in scount:
#                 smaller.append(scount[num])
#             else:
#                 count = 0
#                 for n in nums:
#                     if num > n:
#                         count += 1
#                 smaller.append(count)
#                 scount[num] = count
#         return smaller

# Time : O(Nlog N) Space : O(N)


class Solution:
    def smaller_than_current(self, nums: List[int]) -> List[int]:
        sorted_num = sorted(nums)
        prev = sorted_num[0]
        smaller_than = {prev: 0}
        for idx in range(1, len(sorted_num)):
            if(sorted_num[idx] > prev):
                smaller_than[sorted_num[idx]] = idx
            prev = sorted_num[idx]
        for idx in range(len(nums)):
            sorted_num[idx] = smaller_than[nums[idx]]
        return sorted_num


solution = Solution()
numbers = [1, 29, 362, 22, 33, 22, 33, 12, 0, 33, -1, 362]
print(numbers)
smaller_than = solution.smaller_than_current(numbers)
numbers.sort()
print(numbers)
print(smaller_than)
