class Solution:
    def capitalizeTitle(self, title: str) -> str:
        t=""
        for i in title.split():
          if len(i)>=3:
            t+= i.capitalize()+" "
          else:
            t+= i.lower()+" "
        return t.strip()
         
