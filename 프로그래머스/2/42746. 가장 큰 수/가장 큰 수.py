def solution(numbers):
    if numbers == [0]*len(numbers): return '0'
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x: (x[0], x[1%len(x)], x[2%len(x)], x[3%len(x)]), reverse=True)
    return ''.join(numbers)