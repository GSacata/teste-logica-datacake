num_list = [9, 2, 3, 1, 4]
initial_num_list = num_list.copy()
missing_num_list = []
interval_start = 0
i = interval_start

def find_interval_end(list):
    list.sort()
    return list[-1]

interval_end = find_interval_end(num_list)

while i < interval_end:
    if i in num_list:
        pass # 'i' number already exists in num_list
    else:
        missing_num_list.append(i)
        num_list.append(i)
    
    i += 1

print(f"Results:\nInitial num list: {initial_num_list},\nNumbers missing: {missing_num_list},\nCurrent num list: {num_list} ")