class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split(' ')
        if len(words) != len(pattern):
            return False
        
        return len(set(zip(pattern, words))) == len(set(pattern)) == len(set(words))

def test():
    solution = Solution()
    pattern = "abba"
    s = "dog cat cat dog"
    assert solution.wordPattern(pattern, s) == True

    pattern = "abba"
    s = "dog dog dog dog"
    assert solution.wordPattern(pattern, s) == False

if __name__ == '__main__':  
    test()
    print("Everything passed")