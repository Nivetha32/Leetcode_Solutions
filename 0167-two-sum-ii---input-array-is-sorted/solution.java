class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int left=0;
        int right = numbers.length-1;
        int s=0;
        while(left<right)
        {
            s = numbers[left]+numbers[right];
            if( s == target)
            {
               return new int[]{left+1,right+1};
            }
            else if(s<target)
            {
                  left++;
            }
            else 
            {
                  right--;
            }
          }
         return new int[]{-1,-1};
        }
    }
