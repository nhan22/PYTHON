# Viết chương trình Python chuyển các phần tử dương của danh sách lên đầu danh sách và in
# danh sách ra màn hình.

List = [9, -1, 1, 4, -4, 1, -7, 2, -99, -43, 9, 2, 3, 4, 10, 10, 9, 3, 2, 3, 8, 10, 5, 6, 7, -1, 9, -3, 99, 99, -9, 832, -5, 9, 8, 3, 3, 1, 0]

positives = [] # Danh sách Mới Để lưu trữ các phần tử Dương
minus = [] # Danh sách Mới Để lưu trữ các phần tử Âm

for i in range(len(List)):
    if List[i] > 0:
        positives.append(List[i])

for i in range(len(List)):
    if List[i] <= 0:
        minus.append(List[i])
resutl = positives + minus

print("Danh sách sau khi chuyển các phần tử dương lên đầu:", resutl)