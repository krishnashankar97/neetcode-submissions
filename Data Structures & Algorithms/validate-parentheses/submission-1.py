class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {")" : "(", "]" : "[", "}" : "{"}
        st = []
        for t in s:
            if t in hmap:
                if st and st[-1] == hmap[t]:
                    st.pop()
                else:
                    return False
            else:
                st.append(t)
        return not len(st)