class Path:
    def __init__(self, path):
        self.current_path = path

    def cd(self, new_path):
        result = ''
        current = list(self.current_path.split('/'))

        # Function
        new_path = list(new_path.split('/'))
        for p in new_path:
            if p == '..':
                current.pop(len(current) - 1)
            else:
                current.append(p)
        for idx, c in enumerate(current):
            if idx != 0:
                result += '/' + c
        self.current_path = result


path = Path('/a/b/c/d')
path.cd('../x')
print(path.current_path)
