# v.0.0.0, 14/02/2024
# Status: Ongoing

num_array = [2, 1, 5, 2, 5, 2, 1, 1, 1, 7, 9, 13, 127, 21]
num_one = None
num_n_one = None

def rearrange_item () :
    print("rearrange_item")
    # for index, item in enumerate(num_array):
    #     if item != 1:
    #         num_array.insert(index, 1)
    #     else:
    #         break
    #     print(num_array)

for index_out, item in enumerate(num_array):
    if item == 1:
        print(index_out, item) #DEV-ERASE
        
        for index_in, item in enumerate(num_array):
            if item != 1:
                num_n_one = num_array.pop(index_in)
                print(num_n_one) #DEV-ERASE
                num_array.insert(index_out, num_n_one)    
                num_n_one = None
                break
    else:
        continue

print(num_array)

print("fim") #DEV-ERASE

