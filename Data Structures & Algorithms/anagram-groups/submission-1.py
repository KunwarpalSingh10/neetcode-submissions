class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping charCount to List of Anagrams
        for s in strs:
            count = [0] * 26 # a - z
            for c in s:
                count[ord(c) - ord("a")] += 1 # map to zero
            res[tuple(count)].append(s) # in python list cannot be keys as they are mutable
        return list(res.values())    

        
            
