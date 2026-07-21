class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # brute force
        # n x n
        # visit every substring and add the count of chars into a map
        # if (substr len - max cnt) > k, no
        # <= k -> update max
        
        n = len(s)
        max_count = 0
        for i in range(n):
            chars_cnt = defaultdict(int)
            max_in_range = 0
            for j in range(i, n):
                j_char = s[j]
                chars_cnt[j_char] += 1
                max_in_range = max(max_in_range, chars_cnt[j_char])
                if (j - i + 1) - max_in_range <= k:
                    max_count = max(max_count, j-i+1)
        return max_count
