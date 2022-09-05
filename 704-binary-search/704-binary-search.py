class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # try:
        #     return nums.index(target)
        # except ValueError:
        #     return -1
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            pivot = (left + right) // 2
            if target == nums[pivot]:
                return pivot
            elif target > nums[pivot]:
                left = pivot + 1
            # elif target < nums[pivot]:
            else:
                right = pivot - 1
        
        return -1
                
                
        
        
