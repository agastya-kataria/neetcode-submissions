class Solution {
    public int[] topKFrequent(int[] nums, int k) {

        if(k == nums.length){
            return nums;
        }

        HashMap<Integer, Integer> ans = new HashMap<>();

        for(int n: nums){
            if (ans.containsKey(n)) ans.replace(n,ans.get(n)+1);
            else ans.put(n,1);
        }
        PriorityQueue<Integer> pq = new PriorityQueue<>(
            (a,b) -> ans.get(a)- ans.get(b));

            for (int n: ans.keySet())
            {
                pq.add(n);
                if(pq.size()>k) pq.remove();

            }

            int[] a = new int[k];
            for (int i = 0; i<k; i++){
                a[i] = pq.remove();
            }

            return a;
            
        


        
    }
}
