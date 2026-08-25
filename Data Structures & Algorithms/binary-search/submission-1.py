class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid  # Return index of target
            elif nums[mid] < target:
                left = mid + 1  # Target is in the right half
            else:
                right = mid - 1  # Target is in the left half
                
        return -1