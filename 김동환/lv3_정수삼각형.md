![image](https://user-images.githubusercontent.com/89527573/235092216-66891b58-fcd4-49a5-a7af-af989193366e.png)

# Idea
----
1. 삼각형은 이런 모양
0
01
012
0123
2. 0번은 다음 줄 01에 1번은 다음 줄 12에 영향을 준다.
3. 그러면 다음 줄 0,1은 dp[N번째 줄][줄에서의 위치]를 업데이트하면 된다.
4. 새로운 값이 들어오려고 할 때, dp에 저장된 값과 새로운 값의 후보군 = 현재 위치 & 다음 줄의 값을 비교하면 된다.
5. 마지막 줄을 더 갈 곳이 없으므로 마지막 줄의 전까지만 실행하고 맥스 값을 반환

# Solution
----
````
def solution(triangle):
    answer = 0
    from copy import deepcopy
    dp = deepcopy(triangle)

    for idx,row in enumerate(triangle):
        if idx < len(triangle) -1 :
            for i in range(len(row)):
                dp[idx+1][i] = max(dp[idx][i] + triangle[idx+1][i], dp[idx+1][i])
                dp[idx+1][i+1] = max(dp[idx][i] + triangle[idx+1][i+1], dp[idx+1][i+1])

    return max(dp[-1])
