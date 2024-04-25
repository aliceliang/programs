class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        tmp = ""
        for i in range(len(s)//2):
            tmp = s[i]
            s[i] = s[-i-1]
            s[-i-1] = tmp

        """
        Better solution using 2 pointers:
        i,j = 0,len(s)-1
        while i<=j:
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
        """


def test():
    solution = Solution()
    input = ["h","e","l","l","o"]
    output = ["o","l","l","e","h"]
    solution.reverseString(input)
    assert input == output

    input = ["H","a","n","n","a","h"]
    output = ["h","a","n","n","a","H"]
    solution.reverseString(input)
    assert input == output

if __name__ == '__main__':  
    test()
    print("Everything passed")