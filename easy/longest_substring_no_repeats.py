class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        Given a string s, find the length of the longest substring without repeating characters.

        :type s: str
        :rtype: int
        """
        curr = ""
        ans = 0
        if s == "":
            return 0
        if len(s) == 1:
            return 1
        
        for i in range(len(s)):
            print(s[i], curr)
            if s[i] in curr:
                curr = curr[curr.find(s[i]) + 1:]
            curr += s[i]
            ans = max(ans, len(curr))
        return ans

def test():
    solution = Solution()
    input = "abcabcbba"
    output = 3
    print(solution.lengthOfLongestSubstring(input))
    assert solution.lengthOfLongestSubstring(input) == output

    input = "bbbbb"
    output = 1
    assert solution.lengthOfLongestSubstring(input) == output

if __name__ == '__main__':  
    test()
    print("Everything passed")