# Pergunta 2.1: código alternativo da Pergunta 2
# Criada para treinar e exercitar árvore binária

class Node:
    def __init__(self, node_value):
        self.node_value = node_value
        self.node_l_br = None
        self.node_r_br = None
    
    # def __str__(self) -> str:
    #     return f"node_value: {self.node_value},\nnode_l_br: {self.node_l_br},\nnode_r_br: {self.node_r_br}"
    
    
# def search_node():

n1 = Node(2) #DEV-ER
n2 = Node(5)
print(f'{vars(n1)}\n{vars(n2)}') #DEV-COM
# print(vars(n1)) #DEV-COM