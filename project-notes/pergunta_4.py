num_list = [9, 2, 3, 1, 4]
initial_num_list = num_list.copy()
missing_num_list = []

def find_biggest_num(list):
    list.sort()
    return list[-1]

biggest_num = find_biggest_num(num_list)

print(f"biggest_num, {biggest_num}") # DEV-ERASE