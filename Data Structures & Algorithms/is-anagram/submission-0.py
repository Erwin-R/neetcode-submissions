class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check length
        # Add string into a hashmap and count occurance
        # of each character for both strings
        # (do this with a loop mapping character with count)
        # At the end check if they are both equal 

        if len(s) != len(t): 
            return False

        mapS = {}
        mapT = {}

        for i in range(len(s)):
            mapS[s[i]] = mapS.get(s[i], 0) + 1

        for i in range(len(t)):
            mapT[t[i]] = mapT.get(t[i], 0) + 1      


        return mapS == mapT