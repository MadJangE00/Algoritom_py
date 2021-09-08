# 원형 이중 연결 리스트 구현하기

from __future__ import annotations
from typing import Any, Type

class Node:
    """ 원형 이중 연결 리스트용 노드 클래스 """

    def __init__(self, data: Any = None, prev: Node = None, next: Node = None) -> None:
        """ 초기화 """
        self.data = data
        self.prev = prev or self
        self.next = next or self

class DoubleLinkedList:
    """ 원형 이중 연결 리스트 클래스 """

    def __init__(self) -> None:
        """ 초기화 """
        self.head = self.current = Node()
        self.no = 0

    def __len__(self) -> int:
        """ 연결 리스트의 노드 수를 반환 """
        return self.no

    def is_empty(self) -> bool:
        """ 리스트가 비었는지 확인 """
        return self.head.next is self.head

    def search(self, data: Any) -> Any:
        """ data와 값이 같은 노드를 검색 """
        cnt = 0
        ptr = self.head.next
        while ptr is not self.head:
            if data == ptr.data:
                self.current = ptr
                return cnt
            cnt += 1
            ptr = ptr.next
        return -1

    def __contains__(self, data: Any) -> bool:
        """ 연결 리스트에 data가 포함되어 있는지 판단 """
        return self.search(data) >= 0

    def print_current_node(self) -> None:
        """ 주목 노드를 출력 """
        if self.is_empty():
            print('주목 노드는 없습니다.')
        else:
            print(self.current.data)

    def print(self) -> None:
        """ 모든 노드를 출력 """
        ptr = self.head.next
        while ptr is not self.head:
            print(ptr.data)
            ptr = ptr.next

    def print_reverse(self) -> None:
        """ 모든 노드를 역순으로 출력 """
        ptr = self.head.prev
        while ptr is not self.head:
            print(ptr.data)
            ptr = ptr.prev
    
    def next(self) -> bool:
        """ 주목 노드를 한 칸 뒤로 이동 """
        if self.is_empty() or self.current.next is self.head:
            return False
        self.current = self.current.next
        return True

    def prev(self) -> bool:
        """ 주목 노드를 한 칸 앞으로 이동 """
        if self.is_empty() or self.current.prev is self.head:
            return False
        self.currens = self.current.prev
        return True
    
    def add(self, data: Any) -> None:
        """ 주목 노드 바로 뒤에 노드를 삽입 """
        node = Node(data, self.current, self.current.next)
        self.current.next.prev = node
        self.current.next = node
        self.current = node
        self.no += 1

    def add_first(self, data: Any) -> None:
        """ 맨 앞에 노드를 삽입 """
        self.current = self.head
        self.add(data)

    def add_last(self, data: Any) -> None:
        """ 맨 뒤에 노드를 삽입 """
        self.current = self.head.prev
        self.add(data)