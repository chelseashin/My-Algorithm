우선순위큐(Priority Queue)



```python
import queue

data_queue = queue.PriorityQueue()

data_queue.put((10, "korea"))
data_queue.put((5, 1))
data_queue.put((15, "china"))

data_queue.get()
=> (5, 1)

data_queue.get()
=> (10, 'korea')
```

