class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        Given an integer array nums, return true if you can partition the array into two 
        subsets such that the sum of the elements in both subsets is equal or false otherwise.
        """
        total = sum(nums)
        if nums // 2 == 1:
            return False
        sum = nums / 2
        # check if a subset can sum to the half sum
        nums.sort(reversed = True)
        for i in 

    



def test():
    solution = Solution()
    input = [1,5,11,5]
    assert solution.canPartition(input) == True

    input = [1,2,3,5]
    assert solution.canPartition(input) == False

if __name__ == '__main__':  
    test()
    print("Everything passed")