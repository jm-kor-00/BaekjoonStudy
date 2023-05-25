from collections import deque

deq = deque()

#전단 삽입,삭제 가능
#말단 삽입,삭제 가능
#인덱스 탐색 불가 ex) deque[3] XX

deq.appendleft() #맨앞에 삽입하는 함수
deq.append() #맨뒤에 삽입하는 함수
deq.popleft() #맨 앞에서 꺼내는 함수
deq.pop() #맨 뒤에서 꺼내는 함수

#스택구현은 리스트로도 가능함
stack = deque()
#삽입
stack.append() #말단삽입
#삭제
stack.pop() #말단삭제

#큐 구현
queue = deque()
#삽입
queue.append() #말단삽입
#삭제
queue.popleft() #전단삭제