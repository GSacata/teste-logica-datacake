# Pergunta 2.1: código alternativo da Pergunta 2
# Criada para treinar e exercitar árvore binária



root_node = None
new_node_num = input("create int number node: ")

class Node:
    def __init__(self, node_value):
        self.node_value = node_value
        self.node_l_br = None
        self.node_r_br = None


def create_node(node_num):
    node_num = int(node_num)
    return Node(node_num)

def append_node():
    print("run append_node()")
    pass

def erase_created_node():
    global created_node
    created_node = None
    
created_node = create_node(new_node_num)
print(vars(created_node))

append_node()
erase_created_node()

print(created_node)
# def search_node():

# n1 = Node(2) #DEV-ER
# n2 = Node(5) #DEV-ER
# # print(vars(n1)) #DEV-COM

# print(f'{vars(n1)}\n{vars(n2)}') #DEV-COM