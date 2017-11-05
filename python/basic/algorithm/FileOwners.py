# Implement a group_by_owners function that:

# Accepts a dictionary containing the file owner name for each file name.
# Returns a dictionary containing a list of file names for each owner name, in any order.

# For example, for dictionary
# {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'} the group_by_owners
# function should return
# {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}


class FileOwners:
    @staticmethod
    def group_by_owners(files):
        result = {}
        for k in files:
            if result.get(files[k]) is None:
                result[files[k]] = [k]
            else:
                a = result.get(files[k])
                a.append(k)
                result[files[k]] = a
        return result


files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(FileOwners.group_by_owners(files))
