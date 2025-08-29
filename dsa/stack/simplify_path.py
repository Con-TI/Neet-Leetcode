class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        # Keeps track of directories
        cur = ""
        for c in (path + "/"):
            if c == "/":
                if cur == "..":
                    if stack:
                        stack.pop()
                elif cur != "" and cur !=".":
                    stack.append(cur)
                # Reset after every slash
                cur = ""
                print(stack)
            else:
                cur += c
        
        return "/"+"/".join(stack)