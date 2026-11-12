class Solution:
    def canJump(self, nums: List[int]) -> bool:
        current = 0 
        if nums[current] == 0 and len(nums) != 1: 
            return False
        target = len(nums) - 1
        while current < target :
            if nums[current] <= 0 : 
                while current >= 0 and nums[current] <= 0:
                    current -= 1
                if current < 0 : 
                    return False
            else : 
                nums[current] *= -1
                current += -(nums[current])
        return True