class Solution(object):
    def simplifyPath(self, path):
        # We use a stack to store valid directory names.
        # When we see "..", it means go back one directory, so we pop from the stack.
        # We skip "" (caused by //) and "." (current directory).
        stack = []
        
        # Split path into components using "/" as a delimiter
        # Example: "/a//b/../c" -> ['', 'a', '', 'b', '..', 'c']
        directories = path.split("/")
        
        for dir in directories:
            # Skip empty strings (from "//") or "." (current directory)
            if dir == '' or dir == '.':
                continue
            elif dir == '..':
                # Go back one directory if possible
                if stack:
                    stack.pop()
            else:
                # Add a valid directory to the stack
                stack.append(dir)
        
        # Join everything in the stack with "/" and add a leading "/"
        return "/" + "/".join(stack)
