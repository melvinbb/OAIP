def brackets(line):
    stack = []
    brackets_map = {")": "(", "]": "[", "}": "{", ">": "<"}
    for char in line:
        if char in brackets_map.values():
            stack.append(char)
        elif char in brackets_map:
            if not stack or stack[-1] != brackets_map[char]:
                return False
            stack.pop()
    return not stack
