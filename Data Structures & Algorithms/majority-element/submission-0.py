class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Iterate through array and count numbers with map and return max 

        count = {}
        
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        maxNum = None
        maxCount = 0

        for key, val in count.items():
            if val > maxCount: 
                maxNum = key
                maxCount = val
            

        return maxNum