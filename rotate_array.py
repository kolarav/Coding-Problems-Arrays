from typing import List

#  Brute force solution
# Time : O(N*K) K -> number of rotation  Space : O(1)
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         while(k > 0):
#             i = nums.pop()
#             nums.insert(0, i)
#             k -= 1


# Time : O(N) Space : O(1)


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        start = count = 0
        while count < n:
            current, prev = start, nums[start]
            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1

                if start == current:
                    break
            start += 1


numbers = [i for i in range(1000000)]
# print(numbers)
solution = Solution()
solution.rotate(numbers, 1000000)
# print(numbers)
