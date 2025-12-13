class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        
        int o= m - 1;    
        int p= n - 1;   
        int q= m + n - 1; 

        while (o>= 0 && p>= 0) {
            if (nums1[o] > nums2[p]) {
                nums1[q] = nums1[o];
                o--;
            } else {
                nums1[q] = nums2[p];
                p--;
            }
            q--;
        }

       
        while (p>= 0) {
            nums1[q] = nums2[p];
            p--;
            q--;
        }
    }
}
