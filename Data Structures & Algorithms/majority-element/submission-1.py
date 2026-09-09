class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Iterate through array and count numbers with map and return max 

        res = 0 # Current candidate
        count = 0 # current count

        for num in nums:
            if count == 0:
                res = num
            
            count += 1 if num == res else -1

        return res