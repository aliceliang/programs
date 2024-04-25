class Solution(object):
    def kth_largest_element(self, nums, k):
        """
        Given an array nums representing wood piece lengths, we want to make K equal length pieces. What is the maximum length of these equal pieces?
            Arr = [5,4,9,3], K = 3
            Ans: = 4 because we can make (5 = 4+1, 4, 9 = 4+5)

            Arr = [5,4,9,3], K = 2
            Ans: = 5

            Arr = [110,5,7,3] K = 2
            Ans = 55 because we can make (110 = 55 + 55)

        sort the array: [5, 4, 9 3] k = 3
        [5] : 1  compare 5 and k => divide
        [5, 4]: 2 compare 5, 4, 
            is len 2 possible? [5, 4] -> [2, 2, 1, 2, 2] -> count(2) > k, 2 is possible, update max_length
            is len 3 possible? [3, 2, 3, 1] -> count(3) < k, 3 is not possible
        [5, 4, 9, 3]
        max_possible = sum(nums)/k  or max(nums)
        min_possible = 1

        pick length = (max + min)/ 2
        pick next length = (curr + max)/2
        """
    def maxLength(self, lengths, k):
        max_possible = sum(lengths) / k 
        min_possible = 1
        
        while min_possible < max_possible:
            try_length = (min_possible + max_possible) / 2
            num_cuts = [i // try_length for i in lengths]
            if sum(num_cuts) >= k:
                min_possible = try_length
            else:
                max_possible = try_length
        return min_possible
            
def test():
    solution = Solution()
    input = [7,4,1,9,4]
    print(solution.removeParentheses(input))

    input = "lee(t)c(od(e)"
    print(solution.removeParentheses(input))

    input = "a)b(c)d"
    print(solution.removeParentheses(input))

    input = "))(("
    print(solution.removeParentheses(input))

if __name__ == '__main__':  
    test()
    print("Everything passed")