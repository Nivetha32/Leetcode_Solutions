class Solution {
    private int ref(int n)
    {
        String r = Integer.toBinaryString(n);
        String d = new StringBuilder(r).reverse().toString();
        return Integer.parseInt(d,2);
    }
    public int[] sortByReflection(int[] nums) {
        int k = nums.length;
        int[][]p = new int[k][2];
        for(int i=0;i<k;i++)
            {
                p[i][0]=nums[i];
                p[i][1]=ref(nums[i]);
            }
        Arrays.sort(p,(u,v)->
                    {
                        if(u[1]!=v[1])
                        {
                            return u[1]-v[1];
                        }
                        return u[0]-v[0];
                    });
        for(int i=0;i<k;i++)
            {
                nums[i]=p[i][0];
            }
        
        return nums;
    }
}
