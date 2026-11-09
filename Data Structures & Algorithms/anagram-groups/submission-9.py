class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            hashmap[tuple(sorted(s))].append(s)

        return list(hashmap.values())