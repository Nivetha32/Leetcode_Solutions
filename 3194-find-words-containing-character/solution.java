class Solution {
    public List<Integer> findWordsContaining(String[] words, char x) {
        List<Integer> k = new ArrayList<Integer>();
        for(int i=0;i<words.length;i++)
        {
            if(words[i].indexOf(x)!=-1)
            {
                k.add(i);
            }
        }
        return k;
    }
}
