class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carryover = 0
        output = []
        for i in range(1, max(len(a), len(b)) + 1):
            a_selection = int(a[-i]) if len(a) >= i else 0
            b_selection = int(b[-i]) if len(b) >= i else 0                
            sum = a_selection + b_selection + carryover
            carryover = 1 if sum >= 2 else 0
            output.append(str(sum % 2))
        if carryover == 1:
            output.append(str(carryover)) 
        output.reverse()
        return ''.join(output)

def test():
    solution = Solution()  
    assert solution.addBinary("1111", "1111") == "11110"    

if __name__ == '__main__':  
    test()
    print("Everything passed")