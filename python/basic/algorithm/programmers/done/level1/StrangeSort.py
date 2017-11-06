from operator import itemgetter


def strange_sort(strings, n):
    '''strings의 문자열들을 n번째 글자를 기준으로 정렬해서 return하세요'''
    return sorted(strings, key=itemgetter(n))


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(strange_sort(["sun", "bed", "car"], 1))


# Another Good answer
def strange_sort(strings, n):
    '''strings의 문자열들을 n번째 글자를 기준으로 정렬해서 return하세요'''
    return sorted(strings, key=lambda x: x[n])


strings = ["sun", "bed", "car"]
print(strange_sort(strings, 1))
