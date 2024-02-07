N, M = map(int, input().split(" "))
A = list(map(int, input().split(" ")))
B = list(map(int, input().split(" ")))
print(len(A)+len(B)-2*len(set(A) & set(B)))