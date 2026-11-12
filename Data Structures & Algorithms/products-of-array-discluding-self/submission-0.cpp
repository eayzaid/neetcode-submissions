class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int>nums1(nums.size());
        vector<int>nums2(nums.size());
        nums1[nums.size() - 1] = nums[ nums.size() -1];
        nums2[0] = nums[0];

        for(int i = 1 ; i < nums.size() ; i++){
            nums2[i] = nums[i] * nums2[i-1];
            nums1[nums.size() - 1 - i] = nums[nums.size() - 1 - i] * nums1[nums.size() - i ];
        }
        vector<int> result (nums.size());
        for(int i = 0 ; i < nums.size(); i++){
            if( i == 0){
                result[i] = nums1[i+1];
            }else if ( i == nums.size() - 1){
                result[i] = nums2[i - 1];
            }else{
                result[i] = nums2[i - 1] * nums1 [ i+1 ];
            }
        }
        return result;
    }
};
