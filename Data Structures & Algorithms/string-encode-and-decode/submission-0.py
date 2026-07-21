class Solution:

    def encode(self, strs: List[str]) -> str:
        to_merge = []
        for s in strs:
            to_merge.append(str(len(s)) + '#' + s)
        return ''.join(to_merge)

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded = []
        while i < len(s):
            # find length
            j = i
            while s[j] != '#':
                j += 1
            n = int(s[i:j])
            i = j+1
            decoded.append(s[i:i+n])
            i = i+n
        return decoded
