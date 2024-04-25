class Solution(object):
    def subarray_sum(self, nums, k):
        """
        Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

        A subarray is a contiguous non-empty sequence of elements within an array.

        # look up a O(N) solution

        Example 1:
        Input: nums = [1,1,1], k = 2
        
        Output: 2

        Example 2:
        Input: nums = [1,2,3], k = 3
        Output: 2

        Input: nums = [1,1,-1, 3, -1], k = 2
        Output: 2

                Constraints:
        1 <= nums.length <= 2 * 104
        -1000 <= nums[i] <= 1000
        -10^7 <= k <= 10^7

        """
        result = 0
        sums = [[i for i in range(len(nums))] for _ in range(len(nums))]
        for i in range(len(nums)): # i = 0
            for j in range(i, len(nums)): # [1, 2, 3] [0, 1, 2]
                if j == i:
                    sums[i][j] = nums[i]
                elif j == i + 1:
                    sums[i][j] = nums[i] + nums[j]
                else:
                    sums[i][j] = sums[i][j-1] + nums[j]
                if sums[i][j] == k:
                    result += 1
        return result

def test():
    solution = Solution()
    input = [1,1,1]
    output = 2
    print(solution.subarray_sum(input, 2))
    assert solution.subarray_sum(input, 2) == output

    input = [1,2, 3]
    output = 2
    print(solution.subarray_sum(input, 3))
    assert solution.subarray_sum(input, 3) == output

    input = [1,1,-1, 3, -1]
    output = 4
    print(solution.subarray_sum(input, 2))
    assert solution.subarray_sum(input, 2) == output

if __name__ == '__main__':  
    test()
    print("Everything passed")