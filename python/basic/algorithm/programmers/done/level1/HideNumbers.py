def hide_numbers(s):
    return '*' * (len(s) - 4) + s[-4:]


print("결과 : " + hide_numbers('01033334444'));


# def hide_numbers(s):
#     return '*'*len(s[:-4]) + s[-4:]


# import re
#
# def hide_numbers(s):
#     p = re.compile(r'\d(?=\d{4})')
#     return p.sub("*", s, count = 0)
#
# # 아래는 테스트로 출력해 보기 위한 코드입니다.
# print("결과 : " + hide_numbers('01033334444'));
# print("결과 : " + hide_numbers('027778888'));
