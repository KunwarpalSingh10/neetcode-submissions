class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #sorted() returned sorted list of characters
        return sorted(s) == sorted(t)