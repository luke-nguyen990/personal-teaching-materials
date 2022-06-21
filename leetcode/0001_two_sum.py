# https: // leetcode.com/problems/two-sum/


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices_map = dict()
        for index, value in enumerate(nums):
            if (target - value) in indices_map:
                return [indices_map[(target - value)], index]
            indices_map[value] = index
