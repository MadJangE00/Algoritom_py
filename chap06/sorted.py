# 정렬을 마친 두 배열의 병합(heapq.merege 사용)

import heapq

a = [2, 4, 6, 8, 11, 13]
b = [1, 2, 3, 4, 9, 16, 21]
c = list(heapq.merge(a,b))

if __name__ == '__main__':
    print(a)
    print(b)
    print(c)

