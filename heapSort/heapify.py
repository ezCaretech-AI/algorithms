def heapify(input_array, index, heap_size):
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < heap_size and input_array[left_index] > input_array[largest]:
        largest = left_index
    if right_index < heap_size and input_array[right_index] > input_array[largest]:
        largest = right_index
    if largest != index:
        input_array[largest], input_array[index] = input_array[index], input_array[largest]
        heapify(input_array, largest, heap_size)