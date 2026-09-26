class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Identify Problem: Sliding Window being asking for substring's length under some condition.
        Approach: Having a l and r for idetifying boundaries of sliding window and we want a hashmap that identifies the most occuring character within the substring. We will use that in order to find the number of characters that need to be replaced inside the substring by subtracting it by the length of the string. We move the left pointer only when there are more characters than need to be replaced than k.
        Time Complexity: O(n), we are just iterating over the string s a single time
        Space Complexity: O(n), we are going to store the characters of the string inside hashmap
        """
        hashmap = defaultdict(int)
        l = 0
        longest = 0

        for r in range(len(s)):
            hashmap[s[r]] += 1
            while (r - l + 1) - max(hashmap.values()) > k:
                hashmap[s[l]] -= 1
                l += 1
            longest = max(r - l + 1, longest)
        
        return longest
