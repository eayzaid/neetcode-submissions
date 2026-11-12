class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        suf = [nums[0]]*n
        pref = [nums[n-1]]*n
        for i in range(1,n):
            suf[i] = suf[i-1] * nums[i]
            pref[n-i-1] = pref[n-i] * nums[n-i-1]
        ans = []
        for i in range(n):
            if i == 0 : 
                ans.append(pref[1])
            elif i == n - 1 :
                ans.append(suf[n-2])
            else : 
                ans.append(suf[i-1]*pref[i+1])
        return ans