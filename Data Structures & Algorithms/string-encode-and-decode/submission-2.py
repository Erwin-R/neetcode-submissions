class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for w in strs: 
            res += str(len(w)) + "#" + w

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        # 5#Hello5#World
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i: j])
            
            i = j + 1
            res.append(s[i: i + length])
            
            i += length

        return res
