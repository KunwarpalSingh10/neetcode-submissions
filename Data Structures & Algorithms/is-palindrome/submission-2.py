class Solution:
    def isPalindrome(self, s: str) -> bool:
        sort = ""
        for c in s:
            if (ord(c) >= 65 and ord(c) <= 90) or (ord(c) >= 97 and ord(c) <= 122) or (ord(c) >= 48 and ord(c) <= 57):
                sort += c
        sort = sort.lower()
        # print(sort)

        length = len(sort)

        if length % 2 == 0:
            l = (length // 2) - 1
            r = (length // 2)
        else:
            l = length // 2
            r = length // 2
        while l >= 0 and r < length:
            if sort[l] != sort[r]:
                return False
            l -= 1
            r += 1
        return True

        
                
        