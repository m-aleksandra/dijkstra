class PriorityQueue:
    def __init__(self):
        self.heap = []  # stores tuples (distance, node)
    
    def empty(self) -> bool:
        return not self.heap
    
    def _parent(self, i) -> int:
        return (i - 1) // 2
    
    def _left_child(self, i) -> int:
        return 2 * i + 1
    
    def _right_child(self, i) -> int:
        return 2 * i + 2
    
    def _swap(self, i, j) -> None:
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _heapify_up(self) -> None:
        curr_idx = len(self.heap) - 1

        while curr_idx > 0:
            parent_idx = self._parent(curr_idx)
            if self.heap[curr_idx][0] < self.heap[parent_idx][0]:
                self._swap(curr_idx, parent_idx)
                curr_idx = parent_idx
            else:
                break
    
    def _heapify_down(self) -> None:
        curr_idx = 0
        size = len(self.heap)

        while curr_idx < size // 2:
            left_child_idx = self._left_child(curr_idx)
            right_child_idx = self._right_child(curr_idx)
            smallest = curr_idx

            if left_child_idx < size and self.heap[left_child_idx][0] < self.heap[smallest][0]:
                smallest = left_child_idx
            if right_child_idx < size and self.heap[right_child_idx][0] < self.heap[smallest][0]:
                smallest = right_child_idx

            if smallest == curr_idx:
                break
            else:
                self._swap(curr_idx, smallest)
                curr_idx = smallest

    def push(self, item) -> None:
        self.heap.append(item)
        self._heapify_up()

    def pop(self) -> tuple:
        if self.empty():
            return None  
        self._swap(0, len(self.heap) - 1)
        min_item = self.heap.pop()
        self._heapify_down()
        return min_item
    


# Test the priority queue with the tasks and priorities
def main():
    pq = PriorityQueue()  # Initialize your priority queue

    # Adding tasks to the priority queue
    pq.push((2, 5))  # Priority 2, Task ID 5
    pq.push((1, 3))  # Priority 1, Task ID 3
    pq.push((4, 10)) # Priority 4, Task ID 10
    pq.push((3, 1))  # Priority 3, Task ID 1
    pq.push((5, 7))  # Priority 5, Task ID 7

    # Popping tasks from the priority queue and printing them
    while not pq.empty():
        priority, task_id = pq.pop()
        print(f"Task ID: {task_id}, Priority: {priority}")

if __name__ == "__main__":
    main()

