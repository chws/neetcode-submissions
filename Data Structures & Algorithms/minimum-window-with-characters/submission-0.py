class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # we need three variables to track
        # left, right pointers
        # dictionary where they have the char and its number
        # int variable to track how many char & its number is matching to 't'
        if len(s) < len(t):
            return ""
        t_dict = Counter(t)
        need = len(t_dict)
        left = 0
        window = defaultdict(int)
        have = 0
        res_len = len(s) + 1
        res = ""
        for right in range(len(s)):
            window[s[right]] += 1
            if window[s[right]] == t_dict[s[right]]:
                have += 1
            
            # let's move left till have != need
            while have == need:
                if (right - left + 1) < res_len:
                    res_len = right - left + 1
                    res = s[left:right+1]

                window[s[left]] -= 1
                if window[s[left]] < t_dict[s[left]]:
                    # have only decreases when window's count is less the t's count
                    have -= 1
                left += 1
        return res