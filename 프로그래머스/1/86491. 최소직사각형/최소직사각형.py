def solution(sizes):
    w, h = 0, 0
    for card in sizes:
        a, b = (card[0], card[1]) if card[0] > card[1] else (card[1], card[0])
        if w < a: w=a
        if h < b: h=b
    return w*h