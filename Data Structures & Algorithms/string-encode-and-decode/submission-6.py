class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for s in strs:
            enc += str(len(s))
            enc += "#"
            enc += s
        print(enc)
        return enc
        
            
    def decode(self, s: str) -> List[str]:
        temp = ""
        ans = []
        i = 0

        while i < len(s):
            if s[i] == "#":
              ans.append(s[i+1:i+int(temp)+1])
              i = i + int(temp) + 1
              temp = ""  
            else:
              temp += s[i]
              i += 1

        return ans