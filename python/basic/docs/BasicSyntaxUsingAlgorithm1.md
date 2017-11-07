# Python Syntax and Grammar Summary through Algorithm 1

- Author : [SeolHun](https://github.com/SeolHun)
- CreatedDate : 2017.11.07

---
## 1. map(function, iterable)
1. map은 입력받은 자료형의 각 요소가 함수 f에 의해 수행된 결과를 묶어서 리턴하는 함수이다.
2. 간단하게 얘기해서 해당 Object에 Function을 적용시켜주는 구문이라고 생각합니다 

- Question : [Lv2 : Palindrom](https://programmers.co.kr/learn/challenge_codes/85)
	```python
	def digit_reverse(n):
    	return list(map(int, str(n)[::-1]))
	print("결과 : {}".format(digit_reverse(12345)));
	```
- Process 
    1. 만약, reversed(n) or n[::-1]을 사용하면 아래와 같은 타입 에러를 발생시킨다
        - TypeError: 'int' object is not subscriptable
        - 인트는 Object가 아니여서 TypeError가 발생된다
        ```python
        class reversed(object):
        ```
    2. map을 사용하여 int => object로 바꾼다
    - 가볍게 int 함수를 봐보자
    ```python
    class int(object):
      """
      int(x=0) -> integer
      int(x, base=10) -> integer
    ```
    ```python
    map(int, str(n)[::-1] or reversed(s))
    ```
    
    3. 마지막으로, 가볍게 list()로 [5,4,3,2,1] 값으로 바꿔줍니다

