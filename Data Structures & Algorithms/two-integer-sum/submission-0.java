class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] pair = new int[2];
        for(int i = 0; i<nums.length; i++){
            int x = target - nums[i];
            for(int j=i+1; j<nums.length; j++){
                if (x==nums[j])
                {
                    pair[0] = i;
                    pair[1] = j;
                    Arrays.sort(pair);
                    return pair;
                }
            }
        }
        return null;
    }
}
