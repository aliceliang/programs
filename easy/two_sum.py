class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = 1
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    return [i, j]
                j += 1
            i += 1
            
    def twoSumLinear(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers) - 1 # 0, 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return left + 1, right + 1
            elif total < target:
                left += 1
            else:
                right -= 1
        