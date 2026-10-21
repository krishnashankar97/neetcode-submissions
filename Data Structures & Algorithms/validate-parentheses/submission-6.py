class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        sttoopen = {')':'(','}':'{',']':'['}

        for b in s:
            if b in sttoopen:
                if st and st[-1] == sttoopen[b]:
                    st.pop()
                else:
                    return False
            else:
                st.append(b)
        
        return not(len(st))