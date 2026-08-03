class Solution:
    def romanToInt(self, s: str) -> int:
        k = 'Z' + s
        
        main = {
            'Z': 0,
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        sub = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }

        number = 0
        i = 1  

        while i < len(k):
            temp = k[i-1] + k[i]
            if temp in sub:
                number += sub[temp]
                r, _, z = k.partition(temp)
                k = r + z
                i = 1  
            else:
                i += 1


        for char in k:
            number += main[char]

        return number
