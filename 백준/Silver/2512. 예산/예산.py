N = int(input())
budget = list(map(int, input().split()))
M = int(input())

if sum(budget) <= M :
    print(max(budget))
elif min(budget) > M//N:
    print(M//N)
else:
    budget.sort()
    _min, _max = min(budget), max(budget)
    while _min <= _max:
        mid = (_min + _max) // 2
        res = 0
        for i in budget:
            res += (mid if i > mid else i)
        if res > M:
            _max = mid - 1
        else:
            _min = mid + 1
    print(_max)