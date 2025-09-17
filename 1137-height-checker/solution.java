class Solution {
    public int heightChecker(int[] heights)
     {
        int count=0;
        int c[] = new int[heights.length];
        for(int i=0;i<heights.length;i++)
        {
            c[i]=heights[i];
        }
        Arrays.sort(c);
        for(int i=0;i<heights.length;i++)
        {
            if(heights[i] != c[i])
                {
                      count++;
                }
           
        }
        return count;
        
    }
}
