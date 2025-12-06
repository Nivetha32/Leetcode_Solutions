class Solution {
    boolean isDi(int n)
    {
        String b  = Integer.toBinaryString(n);
        int f =0, i = b.length()-1;
        while(f<i)
            {
                if(b.charAt(f)!=b.charAt(i)) return false;
                f++;
                i--;
            }
        return true;
    }
    public int[] minOperations(int[] nums) {
        int l = nums.length;
        int[] m = new int[l];
        for(int i=0;i<l;i++)
            {
                int h = nums[i];
                int u = h;
                while(u>=0 && ! isDi(u))
                    {
                        u--;
                    }
                int v = h;
                while(!isDi(v))
                    {
                        v++;
                    }
                int li = (u<0 ? Integer.MAX_VALUE : h-u);
                int ji = v-h;
                m[i]=Math.min(li,ji);
            }
        return m;
    }
}
