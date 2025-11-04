class Solution {
    public String simplifyPath(String path) {
        String[] valid = path.split("/");
        Stack<String> fil = new Stack<>();
        for(String dir : valid)
        {
            if(dir.equals("")|| dir.equals("."))
            {
                continue;
            }
            if(dir.equals(".."))
            {
                if(!fil.isEmpty())
                {
                    fil.pop();
                }
            }
            else
            {
                fil.push(dir);
            }
        }
        StringBuilder sb = new StringBuilder();
        while(!fil.isEmpty())
        {
            sb.insert(0,"/"+fil.pop());
        }
        if (sb.length() == 0) {
            sb.append("/");
        }
      return sb.toString();
    }
}
