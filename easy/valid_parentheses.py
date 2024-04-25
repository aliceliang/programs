class Solution(object):
    def isValid(self, s):
        """
        Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

        An input string is valid if:
            Open brackets must be closed by the same type of brackets.
            Open brackets must be closed in the correct order.
            Every close bracket has a corresponding open bracket of the same type.

        :type s: str
        :rtype: bool
        """
        open_brackets = []
        for i in range(len(s)):
            if s[i] in ["(", "[", "{"]:
                open_brackets.append(s[i])
            else:
                match = open_brackets.pop() if open_brackets else ""
                if s[i] == ")" and match != "(":
                    return False
                if s[i] == "]" and match != "[":
                    return False
                if s[i] == "}" and match != "{":
                    return False
                else:
                    continue
        return False if open_brackets else True