class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        hmap = {')':'(','}':'{',']':'['}
        for b in s:
            if b in hmap:
                if st and st[-1] == hmap[b]:
                    st.pop()
                else:
                    return False
            else:
                st.append(b)
        
        return True if not st else False
