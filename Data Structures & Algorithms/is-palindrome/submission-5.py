class Solution:
    def isPalindrome(self, s: str) -> bool:
        sort = ""
        for c in s:
            if c.isalnum():
                sort += c.lower()
        length = len(sort)
        half = length // 2

        if length % 2 == 0:
            l, r = half - 1, half
        else:
            l,r = half, half
        while l >= 0 and r < length:
            if sort[l] != sort[r]:
                return False
            else:
                l -= 1
                r += 1
        return True