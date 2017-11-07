# def longest_palindrom(s):
#     max_value = range(len(s)+1)
#     result = 0
#     for i in max_value:
#         for j in max_value:
#             if s[i:j] == s[i:j][::-1]:
#                 if result < len(s[i:j]):
#                     result = len(s[i:j])
#     return result


def longest_palindrom(s):
    # 함수를 완성하세요
    return len(s) if s[::-1] == s else max(longest_palindrom(s[:-1]), longest_palindrom(s[1:]))


print(longest_palindrom("이늦은밤다들잠들다자꾸만꿈만꾸자"))

