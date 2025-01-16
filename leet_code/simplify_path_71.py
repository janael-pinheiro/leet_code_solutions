class Solution:
    def simplify_path(self, path: str) -> str:
        split_path = path.split("/")
        queue = list(filter(lambda x: x not in ['', '.'], split_path))
        response_stack = []
        while len(queue) > 0:
            current = queue.pop(0)
            while current == ".." and len(response_stack) > 0:
                response_stack.pop(0)
                if len(queue) > 0:
                    current = queue.pop(0)
                else:
                    break
            if current != "..":
                response_stack.insert(0, current)
        return "/" + "/".join(response_stack[::-1])
