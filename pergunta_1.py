# v.0.0.0, 14/02/2024
# Status: Ongoing

num_array = [2, 1, 5, 2, 5, 2, 1, 1, 1, 7, 9, 13, 127, 21]
num_one = None
num_n_one = None

for index_out, item_out in enumerate(num_array):
    if item_out == 1:
        print(index_out, item_out) #DEV-ERASE
        num_one = num_array.pop(index_out)
        
        for index_in, item_in in enumerate(num_array):
            if item_in != 1:
                num_n_one = num_array.pop(index_in)
                print(num_n_one) #DEV-ERASE
                # num_array.insert(index_out, num_n_one)    
                num_array.insert(index_out, num_n_one)
                num_array.insert(0, num_one)
                num_n_one = None
                num_one = None
                break
    else:
        continue

print(num_array)

print("fim") #DEV-ERASE

