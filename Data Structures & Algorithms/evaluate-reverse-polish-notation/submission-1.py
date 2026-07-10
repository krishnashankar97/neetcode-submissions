class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for n in tokens:
            if n == "+":
                st.append(st.pop() + st.pop())
            elif n == "-":
                a,b = st.pop(), st.pop()
                st.append(b - a)
            elif n == "*":
                st.append(st.pop()*st.pop())
            elif n == "/":
                a,b = st.pop(), st.pop()
                st.append(int(float(b/a)))
            else:
                st.append(int(n))
        return st[-1]