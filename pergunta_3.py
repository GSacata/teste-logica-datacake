# receber um número, verificar se é um número inteiro
# faz a soma dos maiores e o crivo
# criar lógica de somas possíveis
# comparar partes das somas com os elementos existentes na lista de números
    # Se ambos existirem na lista, retorna o par e retorna true
    # se um ou ambos não existirem, para para o próximo par
    # se nenhum da lista de pares existir, retorna false

# x = input ("Digite um número inteiro: ")
x = 8 #DEV-ER
num_list = [1, 15, 2, 7, 2, 5, 7, 1, 4]
sum_array = []

# Content: string filter, converting to int and etc.

new_num_list_1 = num_list.copy()
new_num_list_1.sort()

sum_biggest = new_num_list_1[-1] + new_num_list_1[-2]
sum_smallest = new_num_list_1[0] + new_num_list_1[1]

if x > sum_biggest:
    print(f"No combinations available to numbers higher than {sum_biggest}")
elif x <= sum_smallest:
    print(f"No combinations available to numbers lower than {sum_smallest}")
else:
    print("x", x)
    print("run search_combinations()")
    

def create_sum_combo ():
    a, b = 0, x
    
    while a < x:
        sum_pair = (a, b)
        invert_sum_pair = (b, a)

        if invert_sum_pair in sum_array:
            print("pair already exists")
        else:
            sum_array.append(sum_pair)
        a += 1
        b -= 1
    
    print(sum_array)
    print("end create_sum_combo ()")

create_sum_combo ()
