N = int(input())
books = sorted([input() for _ in range(N)])
books_dict = {}
for book in books:
    if book not in books_dict:
        books_dict[book] = 1
    else:
        books_dict[book] += 1

print([k for k,v in books_dict.items() if max(books_dict.values()) == v][0])