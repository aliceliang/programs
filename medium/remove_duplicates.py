class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast = 0, 1
        k = 0
        while fast < len(nums): # 5, 8, 1
            if nums[slow] == nums[fast]: # if they are the same
                k += 1
                if k < 2: # if occurs once or less, we keep it, else we skip
                    nums[slow + 1] = nums[fast]
                    slow += 1
                fast += 1
            else: # they are different
                nums[slow + 1] = nums[fast]
                slow += 1
                fast += 1
                k = 0
        return slow + 1