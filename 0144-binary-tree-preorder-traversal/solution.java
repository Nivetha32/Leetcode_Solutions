/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
         List<Integer> res = new ArrayList<>();
         inorder(root,res);
         return res;
    }
    public void inorder(TreeNode root,List<Integer> re)
    {
        if(root == null) return;
        re.add(root.val);
        inorder(root.left,re);
        inorder(root.right,re);
    }
}
