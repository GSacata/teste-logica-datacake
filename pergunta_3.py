# receber um número, verificar se é um número inteiro
# faz a soma dos maiores e o crivo
# criar lógica de somas possíveis
# comparar partes das somas com os elementos existentes na lista de números
    # Se ambos existirem na lista, retorna o par e retorna true
    # se um ou ambos não existirem, para para o próximo par
    # se nenhum da lista de pares existir, retorna false

# x = input ("Digite um número inteiro: ")

def create_sum_combos (x):
    a, b = 0, x
    
    while a < x:
        sum_pair = (a, b)
        invert_sum_pair = (b, a)

        if invert_sum_pair in sum_array:
            pass # pair already exists
        else:
            sum_array.append(sum_pair)
        a += 1
        b -= 1

def append_sum_combo (x):
    for item in sum_array:
        if item[0] in num_list and item[1] in num_list:
            if item[0] == item[1] and num_list.count(item[0]) == 1:
                pass # Repeated numbers, invalid pair
                return False
            else:
                total_sum_combo.append(item)
        else:
            pass # combination does not exist

def verify_sum_combos (x):
    if x > sum_biggest:
        print(f"No combinations available to numbers higher than {sum_biggest}")
        return False
    elif x <= sum_smallest:
        print(f"No combinations available to numbers lower than {sum_smallest}")
        return False
    else:
        create_sum_combos (x)
        append_sum_combo (x)
    
    if total_sum_combo:
        return True
    else:
        return False

x = 8 #DEV-ER
num_list = [1, 15, 2, 7, 2, 5, 7, 1, 4]
sum_array = []
total_sum_combo = []

# Content: string filter, converting to int and etc.

new_num_list_1 = num_list.copy()
new_num_list_1.sort()

sum_biggest = new_num_list_1[-1] + new_num_list_1[-2]
sum_smallest = new_num_list_1[0] + new_num_list_1[1]
has_combo = verify_sum_combos (x)

print("x =", x)
print("Number List:", num_list)
print(f"Has combo? {has_combo}")
print(f"Available combinations: {total_sum_combo}")
