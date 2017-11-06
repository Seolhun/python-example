# 아래는 테스트로 출력해 보기 위한 코드입니다.

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]

print(list(map(lambda student: student[2], student_tuples)))
print(sorted(student_tuples, key=lambda student: student[2]))
