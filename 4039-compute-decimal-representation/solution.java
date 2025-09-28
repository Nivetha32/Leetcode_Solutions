class Solution {
    public int[] decimalRepresentation(int n) {
       ArrayList<Integer> list = new ArrayList<>();
       int pv=1;
       while(n!=0)
           {
               int k = n%10;
               if(k!=0)
               {
                   list.add(k*pv);
               }
               n/=10;
               pv*=10;
               
           }
        Collections.reverse(list);
        int[] k = new int[list.size()];
        for(int i=0;i<list.size();i++)
            {
                k[i]=list.get(i);
            }
        return  k;
        
    }
}
