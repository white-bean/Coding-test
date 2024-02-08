N, L = map(int, input().split(" "))
location = sorted(list(map(int, input().split(" "))))
result = 1
start = location[0] - 0.5
end = start + L

while location:
    tmp = location.pop(0)
    if tmp > end - 0.5:
        start = tmp - 0.5
        end = start + L
        result += 1
        
print(result)