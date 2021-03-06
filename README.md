# Persistent Priority Queue

A persistent priority queue base with FIFO Queue and LIFO Stack structures.

## Priority Queue
```python
from priorityqueue import PriorityQueue

pq = PriorityQueue("mypq")

pq.push(priority=1, item="world")
pq.push(priority=2, item="hello")

while not pq.is_empty():
    print pq.pop()

# hello
# world
```

## FIFO Queue
```python
from priorityqueue import Queue

q = Queue("myppq")

q.push("hello")
q.push("world")

while not q.is_empty():
    print q.pop()

# hello
# world
```

## LIFO Stack
```python
from priorityqueue import Stack

s = Stack("myppq")

s.push("world")
s.push("hello")

while not s.is_empty():
    print s.pop()

# hello
# world
```

## Unit Tests
```
python test_priorityqueue.python -v
```
