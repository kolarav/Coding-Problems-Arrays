from typing import List


#  This is using hash table or dictionary Time : O(N) space : O(N)
class Solution:
    def single_number(self, nums: List[int]) -> int:
        num_count = {}
        for num in nums:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1

        return(min(num_count, key=num_count.get))


# # This is using bit manupulation. Time : O(N)  space : O(1)
# class Solution:
#     def single_number(self, nums: List[int]) -> int:
#         ans = 0
#         for num in nums:
#             ans ^= num
#         return ans

solution = Solution()
numbers = [1, 2, 3, 5, 2, 5, 2, 7, 7, 3]
print(solution.single_number(numbers))
