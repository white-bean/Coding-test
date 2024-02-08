from itertools import permutations

N, M = map(int, input().split(" "))
nums = list(map(int, input().split(" ")))
for case in sorted(set(permutations(nums, M))):
    print(" ".join(list(map(str, case))))