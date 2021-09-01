# 시퀀스 원소의 최댓값 출력하기

from typing import Any, Sequence

def max_of(a: Sequence) -> Any:
    """시퀀스형 a원소의 최댓값을 반환
    파이썬은 자료형 선언이 자유롭기 때문에 명시적으로 해석하기 어려운 경우가 있다. 이를 위해 주석을 잘 활용하자!"""
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum

if __name__ == '__main__':  #본 파일을 실행한 순간 실행 됨 ( 다른 파일에 임포트 되었으면 실행되지 않음 )
    print('배열의 최댓값을 구합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]값을 입력하세요.: '))

    print(f'최댓값은 {max_of(x)}입니다.')