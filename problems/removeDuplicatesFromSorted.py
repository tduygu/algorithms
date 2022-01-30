"""
Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each
 unique element appears only once. The relative order of the elements should be kept the same.
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print(nums)
        duplicates_list = []
        i = 0
        for i in range(len(nums)):
            if nums.count(nums[i]) > 1:
                x = nums.index(nums[i])
                if i > x:
                    duplicates_list.append(i)
            i += 1

        print(duplicates_list)
        decreasing_index = 0
        for n in duplicates_list:
            nums.pop(n - decreasing_index)
            decreasing_index += 1

        print(nums)
        return len(nums)

abc = [1, 3, 5, 7, 7, 4, 1]
rd = Solution()
rd.removeDuplicates(abc)




