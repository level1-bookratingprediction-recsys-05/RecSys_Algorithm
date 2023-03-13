from collections import deque
def solution(x, y, n):
    if x == y:return 0
    return bfs(x, y, n)


def bfs(x, y, n):
    q = deque()
    q.append((x,y,0))
    visited = set()
    while q:
        x,y, answer = q.popleft()
        if (x, answer) not in visited:
            visited.add((x, answer))
            for new_x in cal(x,n):
                if new_x == y: return answer + 1
                elif new_x < y: q.append((new_x, y, answer + 1))
    return -1 

def cal(x, n):return [x+n, x*2, x*3]
