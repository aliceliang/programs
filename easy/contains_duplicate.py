class Solution(object):
    def containsDuplicate(self, nums):
        """
        Given an integer array nums, return true if any value appears at least 
        twice in the array, and return false if every element is distinct.
        :type nums: List[int]
        :rtype: bool
        """
        found = set()
        for i in nums:
            if i in found:
                return True
            else:
                found.add(i)
        return False