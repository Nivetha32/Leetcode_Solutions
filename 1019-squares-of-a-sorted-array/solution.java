class Solution {
    public int[] sortedSquares(int[] nums) {
        int n = nums.length;
        int arr[] = new int[n] ;
        int left = 0;
        int right = n-1;
        int pos = n-1;
        while(left<=right)
        {
            int lesq = nums[left]*nums[left];
            int rigsq = nums[right]*nums[right];

            if(lesq>rigsq)
            {
                arr[pos]=lesq;
                left++;
            }
            else
            {
                arr[pos]=rigsq;
                right--;

            }
            pos--;
        }
        return arr;
    }
}
