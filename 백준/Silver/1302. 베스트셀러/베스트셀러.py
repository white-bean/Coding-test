N = int(input())
books = sorted([input() for _ in range(N)])
print(max(books, key=books.count))