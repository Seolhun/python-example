def longest_palindrom(s):
    listA = []
    for a in s[2::2]:
        listA.append(a)
    print(listA)


print(longest_palindrom("토마토맛토마토"))
print(longest_palindrom("토마토맛있어"))
