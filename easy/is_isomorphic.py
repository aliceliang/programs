class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_chars = {}
        t_chars = {}
        counter_s = 0
        counter_t = 0
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s_chars.get(s[i]) is None: # i = 1
                s_chars[s[i]] = counter_s  # {a: 0, b: 1}
                counter_s += 1 # counter_s = 2
            if t_chars.get(t[i]) is None:
                t_chars[t[i]] = counter_t # {a: 0}
                counter_t += 1 # counter_t = 1
            if counter_s != counter_t:
                return False
            if s_chars.get(s[i]) != t_chars.get(t[i]):
                return False
        print(counter_s, counter_t)
        print(s_chars, t_chars)
        return True

def test():
    solution = Solution()
    s = "ab"
    t = "aa"
    assert solution.isIsomorphic(s, t) == False

if __name__ == '__main__':  
    test()
    print("Everything passed")