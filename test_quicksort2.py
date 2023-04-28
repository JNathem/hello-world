#implement quicksort algorithm
# Path: test_quicksort3.py
# Compare this snippet from test_sort_3.py:
def quicksort(arr):
     if len(arr) < 2:
            return arr 
        else:
            pivot = arr[0]
            left = [x for x in arr[1:] if x <= pivot]
            print(left)
            right = [x for x in arr[1:] if x > pivot]
            print(right)
            return quicksort(left) + [pivot] + quicksort(right)

print(quicksort([10, 5, 2, 3, -2, 0, 1, 7, 8, 9, 6, 4, 11]))

