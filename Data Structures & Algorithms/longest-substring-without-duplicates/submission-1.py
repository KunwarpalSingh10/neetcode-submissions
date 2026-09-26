class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Identify Problem: This is a sliding window problem because it has you find a substring where it gathered under some condition(s), here being no repeating characters and longest. 
        Approach: left -> 0, right -> 0, set s that stores the string of characters inside the sliding window. The right pointer updates through a loop under the string. The left pointer updates under the condition that the current new character at the right pointer is already in the set, meaning there is a repeat and all those same characters need to be removed, starting from the left. We would also have a longest variable that updates that stores the size of the current longest substring with repeating characters.
        Time Complexity -> O(n), n is the size of the string
        Space Complexity -> O(n), the set stores each character from the string
        """
        l = 0
        sr = set()
        longest = 0

        for r in range(len(s)):
            while s[r] in sr:
                sr.remove(s[l])
                l += 1
            sr.add(s[r])
            longest = max(r - l + 1, longest)

        return longest

            