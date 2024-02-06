N = int(input())
result = N
for i in range(N):
    flag = False
    word = input()
    if len(word) <= 2:
        continue
    else:
        for j in range(0, len(word)-1):
            if word[j] == word[j+1]:
                continue
            elif word[j] in word[j+1:]:
                result -= 1
                break


print(result)