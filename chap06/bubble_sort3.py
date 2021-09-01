# 버블 정렬 알고리즘 구현하기(알고리즘의 개선 2)

from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    """ 버블 정렬(ㅅㅡ캔 범위를 제한) """
    n = len(a)
    k = 0
    while k < n - 1:
        last = n - 1
        for j in range(n - 1, k, -1):
            if a[j - 1] > a[j]:
                a [j - 1], a[j] = a[j], a[j - 1]
                last = j
            k = last
    for i in range(n - 1):
        exchng = 0
        for j in range(n - 1, i , -1):
            if a[j -1] > a[j]:
                a[j -1], a[j] = a[j], a[j -1]
                exchng += 1
        if exchng == 0:
            break

if __name__ == '__main__':
    print('버블 정렬을수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num        # 원소 수가 num인 배열을 생성        

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    bubble_sort(x)          # 배열 x를 버블 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')