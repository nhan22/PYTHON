# Viết chương trình Python sắp xếp danh sách theo thứ tự tăng dần, giảm dần.

List = [9, -1, 1, 4, -4, 1, -7, 2, -99, -43, 9, 2, 3, 4, 10, 10, 9, 3, 2, 3, 8, 10, 5, 6, 7, -1, 9, -3, 99, 99, -9, 832, -5, 9, 8, 3, 3, 1, 0]

selection_sort_up = []
selection_sort_down = []


def swap_selection_up(arr):
    m = len(arr)
    for i in range(m - 1):
        minindex = i
        for j in range(i + 1, m):
            if arr[j] < arr[minindex]:
                minindex = j
        arr[i], arr[minindex] = arr[minindex], arr[i]
    return arr
def swap_selection_down(arr):
    m = len(arr)
    for i in range(m - 1):
        minindex = i
        for j in range(i + 1, m):
            if arr[j] > arr[minindex]:
                minindex = j
        arr[i], arr[minindex] = arr[minindex], arr[i]
    return arr

selection_sort_up = swap_selection_up(List)
print('Mảng theo chiều tăng dần : \n', selection_sort_up)
selection_sort_down = swap_selection_down(List)
print('Mảng theo chiều giảm dần : \n', selection_sort_down)


