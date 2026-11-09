class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        q = sorted(s)
        r = sorted(t)

        return q == r