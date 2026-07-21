class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for num in nums:
            if num-1 not in nums_set:
                curr = num
                curr_length = 0
                while curr in nums_set:
                    curr += 1
                    curr_length += 1
                longest = max(curr_length, longest)
        return longest