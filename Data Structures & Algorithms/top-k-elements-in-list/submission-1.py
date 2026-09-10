class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Map to count each number
        # Once elements are counted we can create an array based on where the count is the index and the number is the value at the index
        # then iterate from array in reverse into a result array

        res = []
        countMap = {}

        for n in nums: 
            countMap[n] = countMap.get(n, 0) + 1

        # Some numbers may occur same number of times so each index has to be an array
        countArr = [[] for i in range(len(nums) + 1)]

        for key, value in countMap.items():
            countArr[value].append(key)
        
        for i in range(len(countArr) - 1, -1, -1):
            for j in range(len(countArr[i])):
                if len(res) == k:
                    break

                res.append(countArr[i][j])

        return res