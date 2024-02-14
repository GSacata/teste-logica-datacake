# v.0.0.0, 14/02/2024
# Status: Ongoing

num_array = [2, 1, 5, 2, 5, 2, 1, 1, 1, 7, 9, 13, 127, 21]
num_is_one = None

for index, item in enumerate(num_array):
    if item == 1:
        print(index, item) #DEV-ERASE
        num_is_one = item
        print(num_is_one) #DEV-ERASE
        break
    else:
        continue

print("fim") #DEV-ERASE

