import queue

data_queue = queue.Queue()

data_queue.put("a")
data_queue.put(1)

data_queue.qsize()
data_queue.get()
