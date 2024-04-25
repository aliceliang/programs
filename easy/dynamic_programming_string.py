class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        Given two strings text1 and text2, return the length of their longest common subsequence.
        A subsequence of a string is a new string generated from the original string with some 
        characters(can be none) deleted without changing the relative order of the remaining characters.
        :type text1, text2: String
        :rtype: String
        """
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        print(dp)
        return dp[0][0]
    
    def longestPalindromeSubseq(self, text):
        dp = [[0] * len(text + 1) for _ in range(len(text) + 1)]
        # we need to keep track of palindromes somehow??
        for i in range(len(text) - 1, -1, -1):
            






def test():
    solution = Solution()
    input1, input2 = "abcdef", "ace"
    output = 3
    assert solution.longestCommonSubsequence(input1, input2) == output

if __name__ == '__main__':  
    test()
    print("Everything passed")

