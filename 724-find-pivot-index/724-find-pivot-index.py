class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0

        for i, num in enumerate(nums):
            if left_sum == total_sum - left_sum - num:
                return i
            left_sum += num

        return -1

# 현재 인덱스에 따라 왼쪽 합 / 오른쪽 합을 구하고 비교하는 방법
# Time Limit Exceeded로 submission을 통과하지 못함
#         pivot_idx = -1
#         for i in range(0, len(nums)):
#             if i == 0:
#                 left_sum = 0
#                 right_sum = sum(nums[i+1: len(nums)])
#             elif i > 0:
#                 left_sum = sum(nums[0: i])
#                 right_sum = sum(nums[i+1:len(nums)])
#             elif i == len(nums) - 1:
#                 left_sum = sum(nums[0:len(nums)])
#                 right_sum = 0

#             if left_sum == right_sum:
#                 pivot_idx = i
#                 break 
        
#         return pivot_idx
                
        