class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        prevSum = {}

        for i in range(len(nums)):
            dif = target - nums[i]

            if dif in prevSum:
                return [prevSum[dif], i]

            prevSum[nums[i]] = i

