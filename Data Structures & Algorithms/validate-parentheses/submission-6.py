class Solution:
    def isValid(self, s: str) -> bool:
            hmap = {"}" : "{", ")" : "(", "]" : "["}
            arr = []
            for c in s:
                if c in hmap:
                    if arr and hmap[c] == arr[-1]:
                        arr.pop()
                    else:
                        return False
                else:
                    print(c)
                    arr.append(c)
            
            return len(arr) == 0