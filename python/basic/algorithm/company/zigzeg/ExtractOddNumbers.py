import re


def get_number(n):
    result = list(filter(lambda x: x % 2 != 0, map(int, re.findall('\d+', n))))
    return sum(pow(x, 2) for x in result)


print(get_number("ab2v9bc13j5jf4jv21"))
