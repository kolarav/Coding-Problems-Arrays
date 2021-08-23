from typing import List


class Solution:
    def replace_elements(self, arr: List[int]) -> List[int]:
        max_rev = [-1]
        for i in range(len(arr)-1):
            if(max_rev[-1] > arr[-1-i]):
                max_rev.append(max_rev[-1])
            else:
                max_rev.append(arr[-1-i])
        max_rev.reverse()
        return max_rev


class Solution:
    def replace_elements(self, arr: List[int]) -> List[int]:
        l = len(arr)-1
        largest = arr[l]
        arr[l] = -1
        l -= 1

        while l >= 0:
            if arr[l] > largest:
                arr[l], largest = largest, arr[l]
            else:
                arr[l] = largest
            l -= 1
        return arr
