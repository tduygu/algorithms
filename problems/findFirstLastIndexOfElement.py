"""
Find First and Last Position of Element in Sorted Array
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
"""


class Solution1(object):
    def search_range(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ind_first = -1
        ind_last = -1
        n = 0
        while n < len(nums):
            if nums[n] == target:
                ind_first = n
                break
            n += 1

        m = -1
        while m > -len(nums):
            if nums[m] == target:
                ind_last = len(nums) + m
                break
            m -= 1

        return [ind_first, ind_last]


nums = [5, 7, 7, 8, 8, 10]
t1 = 8
t2 = 6
sol1 = Solution1()
print(sol1.search_range(nums, t1))
print(sol1.search_range(nums, t2))

nums2 = []
print(sol1.search_range(nums2, t1))






