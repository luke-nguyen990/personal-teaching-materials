# https://leetcode.com/problems/median-of-two-sorted-arrays/

from math import inf
from typing import List


class Solution:

    def findMedianSortedArrays(self, nums1: List[int],
                               nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        total_length = len(nums1) + len(nums2)
        half_length = total_length // 2
        left_pointer, right_pointer = 0, len(nums1)
        while True:
            first_cut = (left_pointer + right_pointer) // 2
            second_cut = half_length - first_cut
            first_lower_median, first_upper_median = -inf, inf
            second_lower_median, second_upper_median = -inf, inf
            if first_cut > 0 and nums1:
                first_lower_median = nums1[first_cut - 1]
            if first_cut < len(nums1):
                first_upper_median = nums1[first_cut]
            if second_cut > 0 and nums2:
                second_lower_median = nums2[second_cut - 1]
            if second_cut < len(nums2):
                second_upper_median = nums2[second_cut]
            if first_lower_median > second_upper_median:
                right_pointer = first_cut - 1
                continue
            if second_lower_median > first_upper_median:
                left_pointer = first_cut + 1
                continue
            if total_length % 2:
                return min(first_upper_median, second_upper_median)
            else:
                return (min(first_upper_median, second_upper_median) + max(first_lower_median, second_lower_median)) / 2
