class Solution {
    public int longestConsecutive(int[] nums) {

        if (nums.length == 0) return 0;

        HashSet<Integer> a = new HashSet<>();

         for(int i=0; i<nums.length; i++){
            a.add(nums[i]);
        }

        int longestSub = 1;

        for (int n : a){
            if (a.contains(n-1)) continue;
            else {
                int currentSub = 1;
                int currentNum = n;
                while(a.contains(currentNum+1)){
                    currentNum++;
                    currentSub++;
                }
                longestSub = Math.max(longestSub, currentSub);
            }
            
        }
        
        return longestSub;
    }
}
