class Solution {
    public int missingMultiple(int[] nums, int k) {
        java.util.HashSet<Integer> set = new java.util.HashSet<>();
    for(int nu : nums)
        {
            set.add(nu);
        }
        int m=k;
        while(set.contains(m))
            {
                m+=k;
            }
        return m;
    }
}
