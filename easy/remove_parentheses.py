class Solution(object):
    def removeParentheses(self, s):
        """
        Given a string s of '(' , ')' and lowercase English characters.

        Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

        Formally, a parentheses string is valid if and only if:

        It is the empty string, contains only lowercase characters, or
        It can be written as AB (A concatenated with B), where A and B are valid strings, or
        It can be written as (A), where A is a valid string.
        
        Example 1:
        Input: s = "lee(t(c)o)de)"
        Output: "lee(t(c)o)de"
        Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

        Input: s = "lee(t)c(od(e)"
        Output: "lee(t)c(ode)" or "lee(t)cod(e)"

        Example 2:
        Input: s = "a)b(c)d"
        Output: "ab(c)d"

        Example 3:
        Input: s = "))(("
        Output: ""
        Explanation: An empty string is also valid.

        Constraints:

        1 <= s.length <= 105
        s[i] is either'(' , ')', or lowercase English letter.
        """
        still_open_parens = 0 # 1
        close_parens = [] # [5]
        open_parens = [] # [3, 7]
        removal = []
        return_string = ""
        for i in range(len(s)):
            if s[i] == "(":
                open_parens.append(i)
                still_open_parens += 1
            elif s[i] == ")":
                close_parens.append(i)
                if still_open_parens > 0:
                    still_open_parens -= 1
                else: #consider this parens for removal
                    removal.append(i)
            else:
                continue
        while still_open_parens > 0:
            removal.append(open_parens[-still_open_parens])
            still_open_parens -= 1

        for i in range(len(s)):
            if i in removal:
                continue
            else:
                return_string += s[i]
        return return_string

def test():
    solution = Solution()
    input = "lee(t(c)o)de)"
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