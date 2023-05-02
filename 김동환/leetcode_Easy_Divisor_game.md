![image](https://user-images.githubusercontent.com/89527573/235090441-62c2af7e-d053-434d-8fd2-3addcbbc10a8.png)

# Idea 
----
1. Alice가 수를 내고 1이 되면 이기고 2가 되면 진다. 
2. 2 -> 1
3. 3 -> 2 -> 1
4. 4 -> 3 -> 2 -> 1
5. 하다 보면 결국 짝수가 나오면 Alice가 이길 수 밖에 없게 되어있다. 

# Solution
----
`````
class Solution:
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0
