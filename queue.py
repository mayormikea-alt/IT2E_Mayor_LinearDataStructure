# Assessment 3.2: Queue (FIFO) Program
# Last Name: MAYOR

from collections import deque

name = "MAYOR"
queue = deque()

print("--- ENQUEUEING LETTERS INTO QUEUE ---")
for letter in name:
    queue.append(letter)
    print(list(queue))

print("\n--- DEQUEUEING LETTERS FROM QUEUE ---")
while len(queue) > 0:
    queue.popleft()
    if len(queue) == 0:
        print("[EMPTY]")
    else:
        print(list(queue))