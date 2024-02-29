# Viết chương trình Python tìm đoạn con có các số hạng dương liên tiếp có tổng lớn nhất. (Nếu
# có nhiều đoạn con thoả mãn thì đưa ra màn hình: Số đoạn con thoả mãn và các đoạn con đó).

List = [9, -1, 1, 4, -4, 1, -7, 2, -99, -43, 9, 2, 3, 4, 10, 10, 9, 3, 2, 3, 8, 10, 5, 6, 7, -1, 9, -3, 99, 99, -9, 832, 10, 20, -5, 9, 8, 3, 3, 1, 0]

max_sum = 0 # Tổng max
max_subarrays = [] # ds lưu đoạn con có sum max
current_sum = 0 # Lưu tổng đoạn con dương hiện tại
current_subarrays = [] # ds lưu đoạn con dương hiện tại

for i in range(len(List)):
    if List[i] > 0:
        current_sum += List[i]
        current_subarrays.append(List[i]) # Thêm số hiện tại vào đoạn con dương hiện tại
    else:
        if current_sum > max_sum:
            max_sum = current_sum # Cập nhật tổng lớn
            max_subarrays = [current_subarrays] # Cập nhật ds đoạn con
        elif current_sum == max_sum:
            max_subarrays.append(current_subarrays) # Thêm đoạn con dương hiện tại vào ds
        current_sum = 0 # Reset tổng đoạn con dương HT
        current_subarrays = [] # Reset đoạn con dương HT
        
# Xử lý TH khi đoạn con dương kết thúc ở cuối ds
if current_sum > max_sum:
    max_sum = current_sum
    max_subarrays = [current_subarrays]
elif current_sum == max_sum:
    max_subarrays.append(current_subarrays)

# In kết quả
print("Tổng lớn nhất của các số hạng dương liên tiếp là:", max_sum)
print("Số lượng đoạn con thoả mãn:", len(max_subarrays))
print("Các đoạn con có tổng bằng", max_sum, "là:")

for ds_con in max_subarrays:
    print(ds_con)