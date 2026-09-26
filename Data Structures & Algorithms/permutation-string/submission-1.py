class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Identify Problem: Sliding Window because your trying to find a substring within another string
        Approach: Use a hashmap for s1 and s2 to count the characters in each. Then we use sliding window to see if those hashmaps ever become equal to each under the condition as we update the count of the characters of s2 according to the window
        Time Complexity: O(n), its iterating through s2 once
        Space Complexity: O(n), where the hashmap stores the characters of s2
        n = The size of s2
        """

        if len(s1) > len(s2):
            return False

        l = 0
        
        hashs1 = defaultdict(int)
        hashs2 = defaultdict(int)

        for c in s1:
            hashs1[c] += 1
        
        for r in range(len(s2)):
            print(hashs2)
            hashs2[s2[r]] += 1
            while (r - l + 1) > len(s1):
                hashs2[s2[l]] -= 1
                if hashs2[s2[l]] == 0:
                    del hashs2[s2[l]]
                l += 1
            if hashs1 == hashs2:
                return True
        return False