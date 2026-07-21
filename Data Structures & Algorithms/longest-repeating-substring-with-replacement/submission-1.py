class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # brute force
        # n x n
        # visit every substring and add the count of chars into a map
        # if (substr len - max cnt) > k, no
        # <= k -> update max

        # we can use sliding window, moving on with right pointer
        # move left only when it exceeds k chars to replace
        # we keep track of the most frequent letter in every window
        
        n = len(s)

        freq = defaultdict(int)
        max_freq_in_window = 0
        left = 0
        result = 0
        for right in range(n):
            freq[s[right]] += 1
            max_freq_in_window = max(max_freq_in_window, freq[s[right]])

            while (right - left + 1) - max_freq_in_window > k:
                # I still don't understand why max_freq_in_window doesn't need to be updated when left moves to the right
                freq[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result
            
