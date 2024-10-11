import heapq

# Initialize an empty priority queue (min-heap by default)
priority_queue = []

# Push elements with their priorities (priority, value)
# Lower priority number means higher priority
heapq.heappush(priority_queue, (2, 'task with priority 2'))
heapq.heappush(priority_queue, (1, 'task with priority 1'))
heapq.heappush(priority_queue, (3, 'task with priority 3'))

# Pop the element with the highest priority (lowest number)
print(heapq.heappop(priority_queue))  # (1, 'task with priority 1')

# Peek the element with the highest priority
print(priority_queue[0])  # (2, 'task with priority 2')
