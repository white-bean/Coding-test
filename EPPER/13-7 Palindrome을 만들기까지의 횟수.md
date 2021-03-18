#### 문제설명
n개의 요소를 갖는 배열 A를 A[i]=A[n-1-i]인 회문을 만들고 싶어한다.<br>
회문이 아닌 배열은 다음 규칙에 따라 수정해 회문을 만들 수 있게 했다.<br>
수정 규칙은 n개의 요소를 갖는 배열이 있을 때, 인접한 요소끼리 합해서 n-1개의 요소를 갖는 배열로 만드는 방법이다.<br>
처음에 회문이 아닌 배열이 주어졌을 때, 몇 번의 수정을 통해 회문이 만들어지는지 그 횟수를 구하는 프로그램을 작성하시오


#### 입력형식
- 첫 번재 줄에 배열을 구성하는 요소의 개수 n을 입력한다(1<=n<=10)
- 두 번째 줄에 n개의 숫자(X)를 공백으로 구분하여 입력한다(1<=X<=100)


#### 코드
```python
def solution(arr, start, end):
	answer = 0
	while arr:                # 배열이 empty가 될 때까지 반복
		if arr[0] == arr[-1]:   # 첫번째 원소와 마지막 원소가 같다면
			arr.pop()             # 둘 다 pop한다
			arr.pop(0)
			#print(arr)

		elif arr[0]<arr[-1]:    # 같지 않고 첫번째 원소가 마지막 원소보다 작다면
			arr[0] = arr.pop(0) + arr[0]  # 첫번째원소와 두번째 원소를 더한다
			#print(arr)
			answer+=1

		else:                   # 같지 않고 마지막 원소가 첫번째 원소보다 작다면
			arr[-1] = arr.pop() + arr[-1] # 마지막 원소와 그 전 원소를 더한다
			#print(arr)
			answer+=1

	return answer

n = int(input())
arr = [int(n) for n in input().split()]

start = int(0);
end = int(n-1);

print(solution(arr, start, end))

```
