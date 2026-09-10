class Solution:

    def encode(self, strs: List[str]) -> str:
        # split strings with delimiters and
        # add in length 5#Hello5#World
        res = []

        for w in strs:
            res.append(str(len(w)))
            res.append("#")
            res.append(w)
        
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        # Iterate through param string
        # capture the length and tell loop to stop when it reaches "#" delim and just append current string to res

        res = []

        # 5#Hello5#World
        i = 0
        while i < len(s): 
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i: j])

            # Once you reach "#" set index to next char in string
            i = j + 1
            
            res.append(s[i: i + length])

            # set i to next length
            i += length
            

        return res