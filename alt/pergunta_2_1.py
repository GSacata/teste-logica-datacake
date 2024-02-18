# Pergunta 2.1: código alternativo da Pergunta 2
# Criada para treinar e exercitar árvore binária


class Node:
    def __init__(self):
        self.value = 0
        self.left_br = {}
        self.right_br = {}

    
    def create_node(self, p_tree, p_value):
        if p_tree.value or p_tree.value == 0:
            if p_value > p_tree.value:
                print("Valor maior eeee")
            else:
                print("Valor menor aaaa")
        else:
            p_tree.value = p_value
            p_tree.left_br = {}
            p_tree.right_br = {}

tree = Node()
print(vars(tree))

tree.create_node(tree, 0)
tree.create_node(tree, 4)
print(vars(tree))