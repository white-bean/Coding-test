from queue import *

q=Queue()

#enqueue
q.put("value")

#dequeue
q.get()




pq=PriorityQueue(10)
#pq.put(("우선순위", "value"))
#우선순위 1, 2, 3, ...
pq.put((3, "abc"))
pq.put((2, "b"))
pq.put((1, "c"))

# 1 -> "c"
# 2 -> "b"
# 3 -> "abc"


