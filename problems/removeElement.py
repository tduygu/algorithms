"""
Given an integer array nums and an integer val, remove all occurrences of val
 in nums in-place. The relative order of the elements may be changed.
"""
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while val in nums:
            nums.remove(val)
        return len(nums)


abc = [1, 2, 3, 4, 5, 6, 6, 1]
re = Solution()
print(re.removeElement(abc, 6))
print(abc)