from random import randint
import copy

def quick_sort(input_array, start, end):
    if (end - start <= 1):
        return

    pivot_index = randint(start, end)
    # pivot_index = 1
    input_array[pivot_index], input_array[end] = input_array[end], input_array[pivot_index]
    pivot = input_array[end]
    left_index = -1
    right_index = 0

    while (right_index != end):
        if input_array[right_index] <= pivot:
           input_array[left_index + 1], input_array[right_index] = input_array[right_index], input_array[left_index + 1]
           left_index += 1

        right_index += 1

    input_array[left_index + 1], input_array[end] = input_array[end], input_array[left_index + 1]
    final_pivot_index = left_index + 1
    
    quick_sort(input_array, start, left_index)
    quick_sort(input_array, final_pivot_index, end)
    
array = [9, 8, 3, 1]*5
for i in range(10):
    array_copy = copy.deepcopy(array)
    quick_sort(array_copy, 0, len(array_copy) - 1)
    print(array_copy)