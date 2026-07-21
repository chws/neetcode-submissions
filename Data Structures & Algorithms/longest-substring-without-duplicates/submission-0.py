class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        # sliding window
        # as we move the right index
        # check if the new letter is already in dict
        # if there is, we move the left to the next one of existing char's index
        left = 0
        max_len = 0
        exist = {} # 'a': 0
        for right in range(n):
            rval = s[right]
            if rval in exist and exist[rval] >= left:
                left = exist[rval] + 1
            exist[rval] = right
            max_len = max(max_len, right - left + 1)
        return max_len