def digit_reverse(n):
    # 함수를 완성해 주세요
    return list(map(int, str(n)[::-1]))

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(digit_reverse(12345)));