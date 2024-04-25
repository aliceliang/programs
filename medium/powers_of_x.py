class Solution(object):
    def power(self, x, n):
        """
        Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

        Example 1:

        Input: x = 2.00000, n = 10
        Output: 1024.00000
        Example 2:

        Input: x = 2.10000, n = 3
        Output: 9.26100
        Example 3:

        Input: x = 2.00000, n = -2
        Output: 0.25000
        Explanation: 2-2 = 1/22 = 1/4 = 0.25
        

        Constraints:

        -100.0 < x < 100.0
        -2^31 <= n <= 2^31-1
        n is an integer.
        Either x is not zero or n > 0.
        -10^4 <= xn <= 10^4

        """
        # x^n = x^(n/2) * x^(n/2)
        # x^n = x^(n-1) * x
        # x^n = (x^(n/2))^2
        # x^(-n) = 1 / x^n

        # if n = 0, return 1
        # if n = 1, return x
        # if n is even, 
            # x^n = (x^(n/2))^2
        # if n is odd:
            # x^(n+1) = ((x^(n/2))^2)*x
        # if n is negative:
            # return 1 / power(x, n)
        # x = 2, n = 10
        if n == 0:
            return 1
        if n == 1:
            return x # return 2
        if n < 0:
            return 1 / self.power(x, n)
        # n > 1:
        if n % 2 == 0: # n is even
            tmp = self.power(x, n/2) # power(2, 5) = 32, power(2, 1) = 2
            return tmp * tmp # 2 * 2, 32 * 32 = 1024
        if n % 2 == 1:
            tmp = self.power(x, n // 2) # power(2, 2) = 4
            return tmp * tmp * x # 4 * 4 * 2 = 32
        
    # nums = [...]
    # get_i(nums, i): true if i < len(nums), otherwise false
    # pick some random number: if get_i(nums, i) == true, double i
    # if false: i = (i + i/2)/ 2
    def powers_iterative(self, x, n):
        if n == 1:
            return x # return 2
        if n < 0:
            return 1 / self.power(x, n)
        # n > 1:
        interval = 1
        k = 2 # current power
        curr = x * x # curr = 4
        while k * 2 < n: # 2 * 2 < 10, 4 * 2 < 10, 8 * 2 > 10
            interval = k # interval = 2, interval = 4
            k *= 2 # k = 4, k = 8
            curr *= curr # curr = 16, curr = 32
        # k*2 > n
        # step it down by interval
        while k + interval > n: # interval = 4, k = 8
            interval /= 2 # interval = 2
        # handle a bunch of if cases:
        if interval == 1:
            return curr * x
        if interval == 2:
            return curr * x * x
        
        
        

            
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