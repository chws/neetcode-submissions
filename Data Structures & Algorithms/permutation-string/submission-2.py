class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # sliding window
        # because the strings contain only lowercase letters
        # keep the map in one array - size of 26
        # and when the two maps match - return True
        # keep track of matching status with a variable.

        if len(s1) > len(s2):
            return False
        
        # calculate the first len(s1) similarity
        s1_map, s2_map = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1_map[ord(s1[i]) - ord('a')] += 1
            s2_map[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if s1_map[i] == s2_map[i]:
                matches += 1

        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True

            right_index = ord(s2[right]) - ord('a')
            left_index = ord(s2[left]) - ord('a')

            s2_map[right_index] += 1            
            if s1_map[right_index] == s2_map[right_index]:
                matches += 1
            elif s1_map[right_index] + 1 == s2_map[right_index]:
                matches -= 1

            # Split right & left because it'll make double count if we don't split
            s2_map[left_index] -= 1
            if s1_map[left_index] == s2_map[left_index]:
                matches += 1
            elif s1_map[left_index] - 1 == s2_map[left_index]:
                matches -= 1
            
            left += 1
        return matches == 26

