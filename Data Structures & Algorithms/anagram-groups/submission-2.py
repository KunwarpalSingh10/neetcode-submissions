class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Explanatory Phase
        res = defaultdict(list) #This creates a empty list val if there is no existing key
        for s in strs: # Going through each string in the list of strings
            count = [0] * 26 # This represents tracking frequency of each character in each str, for a - z
            for c in s: # Going through each character in the current string
                count[ord(c) - ord("a")] += 1 # Increases frequency in count depending on which string it is, ex. b(81) - a(80) = 1, meaning increase frequency of first index
            res[tuple(count)].append(s) # This Accesses the value of the current key(has to be given as tuple, unmutable)
        return list(res.values())





        
            
