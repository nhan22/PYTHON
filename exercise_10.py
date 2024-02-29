#  Viết chương trình Python tìm vị trí bắt đầu đoạn con dương liên tiếp có nhiều phần tử nhất

List = [9, -1, 1, 4, -4, 1, -7, 2, -99, -43, 9, 2, 3, 4, 10, 10, 9, 3, 2, 3, 8, 10, 5, 6, 7, -1, 9, -3, 99, 99, -9, 832, -5, 9, 8, 3, 3, 1, 0]

max_start = -1  # Vị trí bắt đầu của đoạn con dương liên tiếp có nhiều phần tử nhất
max_length = 0  # Độ dài của đoạn con dương liên tiếp có nhiều phần tử nhất
current_start = -1  # Vị trí bắt đầu của đoạn con dương liên tiếp hiện tại
current_length = 0  # Độ dài của đoạn con dương liên tiếp hiện tại


for i in range(len(List)):
   if List[i] > 0:
       if current_start == -1:
           current_start = i
       current_length += 1 
   else:
       if current_length > max_length:
           max_start = current_start
           max_length = current_length
       current_start = -1
       current_length = 0
if current_length > max_length:
    max_start = current_start
if max_start != -1:
    print("Vị trí bắt đầu của đoạn số dương liên tiếp có nhiều phần tử nhất là:", max_start)
else:
    print("Không có đoạn số dương liên tiếp trong danh sách.")