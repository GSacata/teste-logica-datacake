# v.0.0.0, 14/02/2024
# Status: Done

num_array = [2, 1, 5, 2, 5, 2, 1, 1, 1, 7, 9, 13, 127, 21]
required_number = 1
num_one = None
num_n_one = None

def enum_list(list):
    print(f"list: {list}")
    for index, item in enumerate(list):
        print(f"index: {index}, item: {item}")

enum_list(num_array)

# new_num_array = sorted(num_array) # trouxe os 1 para frente, mas muda o index
# enum_list(new_num_array)

for index_out, item_out in enumerate(num_array):
    if item_out == required_number:
        num_one = num_array.pop(index_out)
        
        for index_in, item_in in enumerate(num_array):
            if item_in != required_number:
                num_n_one = num_array.pop(index_in)
                num_array.insert(index_in, num_one)
                num_array.insert(index_out - 1, num_n_one)
                num_n_one = None
                num_one = None
                break
    else:
        continue

enum_list(num_array)


