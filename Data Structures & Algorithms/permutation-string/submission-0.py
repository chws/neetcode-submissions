class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # brute force
        n1 = len(s1)
        s1 = sorted(s1)
        n2 = len(s2)

        for i in range(n2 - n1 + 1):
            curr_str = s2[i:i+n1]
            if s1 == sorted(curr_str):
                return True
        return False
