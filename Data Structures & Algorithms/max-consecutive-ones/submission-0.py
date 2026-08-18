class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        temp = 0
        for i in range (len(nums)):
            if nums[i] == 0:
                if temp > count:
                    count = temp
                temp = 0
            else:
                temp += 1

        if temp > count:
            count = temp

        return count
