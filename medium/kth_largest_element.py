class Solution(object):
    def kth_largest_element(self, nums, k):
        """
        Given an array of ints `nums`, return the kth largest element (0-indexed)
        Nums[7,4,1,9,4], k = 0
        Return 9
        """
        # maintain a list of k largest elements
        # as we iterate, we insert into an ordered list
        # O(N) n = size of nums

        # [7] -> add [9, 7] list is k + 1 length
        # [7, 4] k = 2 
        #   (compare the smallest element) O(1)
        #   (compare the biggest element)  O(1)
        #   (if between, scan the deque) iterate through from the beginning, biggest element first, insert when it's in front O(k)
        #   (cleanup stage) remove last element if len(k_elements) > k
        # O(n * k)

        # merge sort: 
        # compare every 2 -> choose largest (n/2) (n/4) (n/8) -> log(N) 
        # repeat while len(bigger_nums) > 1 
        # Space: O(N)
        # return nums[k]
        
        lists = [[i] for i in nums]
        sorted_list = self.mergesort_helper(lists)
        return sorted_list[k]

    def merge_two_lists(self, list_1, list_2):
        # [1], [2] -> [2, 1]
        # [2, 1], [3, 1] -> [3, 2, 1, 1]
        # [3, 2, 1], [20, 10] i = 0, j = 2 
        i = 0
        j = 0
        merged_list = []
        while i < len(list_1) and j < len(list_2):
            if list_1[i] > list_2[j]:
                merged_list.append(list_1[i])
                i += 1
            else: 
                merged_list.append(list_2[j])
                j += 1
        if i < len(list_1):
            merged_list.append(list_1[i::])
        if j < len(list_2):
            merged_list.append(list_2[j::])
        return merged_list
    
    def quick_sort(self, nums):
        # pick a pivot (first, random, median of medians (nlogn))
        pivot = nums[len(nums)/2]
        left = []
        middle = []
        right = []
        for i in nums:
            if i < pivot:
                left.append(i)
            elif i > pivot:
                right.append(i)
            else:
                middle.append(i)
        left = self.quick_sort(left)
        right = self.quick_sort(right)
        left.extend(middle)
        left.extend(right)
        return left
    
    def mergesort_helper(self, lists):
        # [0], [1], [2]
        if len(lists) == 1:
            return lists

        merged_lists = []
        if len(lists) % 2 == 1:
            merged_lists.append[lists[-1]]
        for i in range((len(lists)) // 2):
            merged_lists.append(self.merge_two_lists(lists[2 * i], lists[2 * i + 1]))
        return self.mergesort_helper(merged_lists)


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