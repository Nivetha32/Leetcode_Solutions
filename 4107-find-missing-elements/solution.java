class Solution {
    public List<Integer> findMissingElements(int[] nums) {
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;

        for(int num: nums)
        {
            min = Math.min(min,num);
            max = Math.max(max,num);
        }
        Set<Integer> mi = new HashSet<>();
        for(int num : nums)
        {
           mi.add(num);
        }
        List<Integer> li = new ArrayList<>();
        for(int i=min;i<=max;i++)
        {
         if(!mi.contains(i))
         {
            li.add(i);
         }
        }
        return li;
    }
}
