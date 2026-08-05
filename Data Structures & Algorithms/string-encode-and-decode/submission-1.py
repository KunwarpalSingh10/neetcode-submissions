class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += s + "4001"
        return encoded
            
    def decode(self, s: str) -> List[str]:
        decoded = []
        new = ""
        c = 0
        while c < len(s):
            if c + 3 < len(s) and s[c] == "4" and s[c+1] == "0" and s[c+2] == "0" and s[c+3] == "1":
                decoded.append(new)
                new = ""
                c += 3
            else:
                new += s[c]
            c += 1
        return decoded

