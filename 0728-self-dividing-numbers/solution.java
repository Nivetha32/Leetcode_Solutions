class Solution {
    public List<Integer> selfDividingNumbers(int left, int right) {
        List<Integer> k = new ArrayList<Integer>();
        for(int i=left;i<=right;i++)
        {
                 boolean self = true;
                 int num=i;
                 while(num!=0)
                 {
                 int dig = num%10;
                 if(dig == 0 ||i%dig!=0 )
                 {
                    self = false;
                    break;
                 }
                 num/=10;
                 }
                 if(self) k.add(i);
        }
        return k;
    }
}
        
