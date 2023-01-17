num = int(input())
for _ in range(num):
    N, M = map(int, input().split())
    im = list(map(int, input().split()))
    id = list(range(len(im)))
    ans = 0
    while im:
        while(im[0] != max(im)):
            im.append(im.pop(0))
            id.append(id.pop(0))
        ans += 1
        if id[0]==M:
            print(ans)
            break
        im.pop(0)
        id.pop(0)
  