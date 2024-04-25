class Solution(object):
    def smallestSubarray(self, arr, s):
        """
        Given an array of positive numbers and a positive number s, find the length 
        of the smallest contiguous subarray whose sum is greater than or equal to s.
        Return 0 if no such subarray exists.
        :type s: List[int]
        :rtype: int
        """
        window_start = 0
        window_sum = 0
        min_window = 10000000

        for window_end in range(len(arr)):
            window_sum += arr[window_end]
            while window_sum >= s:
                min_window = min(min_window, window_end - window_start + 1)
                window_sum -= arr[window_start]
                window_start += 1
        return 0 if min_window == 10000000 else min_window
    
    def longestSubstring(self,str, k):
        """
        Given a string, find the length of the longest substring in it with no more than K distinct characters.
        """
        window_start = 0
        max_length = 0
        window_characters = {}

        for window_end in range(len(str)):

            window_characters[str[window_end]] = window_characters.get(str[window_end], 0) + 1
            
            # if we have more than K distinct characters, we need to move the window start to 
            # remove the last instance of the first
            while len(window_characters) > k:
                print(window_characters, window_start, window_end, max_length)                
                window_characters[str[window_start]] -= 1
                # prune zero
                if window_characters[str[window_start]] == 0:
                    del window_characters[str[window_start]]
                window_start += 1
            max_length = max(max_length, window_end - window_start + 1)
        return max_length




def test():
    solution = Solution()
    input = [2, 1, 5, 2, 3, 2]
    output = 2
    assert solution.smallestSubarray(input, 7) == output

    input = "araaci"
    output = 4
    assert solution.longestSubstring(input, 2) == output

    input = "ardaarciarrr"
    output = 6
    assert solution.longestSubstring(input, 3) == output

if __name__ == '__main__':  
    test()
    print("Everything passed")

