class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(0, len(nums)):
            sum = 0
            for j in range(0, i+1):
                sum += nums[j]
            result.append(sum)
        
        return result
                
                