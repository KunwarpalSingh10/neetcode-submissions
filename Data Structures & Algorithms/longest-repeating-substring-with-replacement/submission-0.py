class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # The idea behind this is that if there are more than k characters in one substring of the nonfrequent characters, we move the left counter forward
        count = defaultdict(int)
        res = 0

        l = 0
        for r in range(len(s)):
            count[s[r]] += 1
            while r - l + 1 - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res