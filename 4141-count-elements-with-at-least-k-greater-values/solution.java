class Solution {
    public int countElements(int[] nums, int k) {
        int arri[] = nums.clone();
        Arrays.sort(arri);
            int nu = arri.length;
        HashMap<Integer,Integer> gr = new HashMap<>();
        for(int i=0;i<nu;i++)
            {
                gr.put(arri[i],nu-1-i);
            }
        int y=0;
        for(int u:nums)
            {
                if(gr.get(u)>=k)
                {
                    y++;
                }
            }
            return y;
    }
}
