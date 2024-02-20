# Pergunta 2.1: código alternativo da Pergunta 2
# Criada para treinar e exercitar árvore binária


print_line = []

class Node():
    def __init__(self, node_value):
        self.value = node_value
        self.left_br = None
        self.right_br = None
    
    def create_node(self, node_value):
        if self.value:
            if node_value > self.value:
                if self.right_br is None:
                    self.right_br = Node(node_value)
                else:
                    self.right_br.create_node(node_value)
            
            elif node_value < self.value:
                if self.left_br is None:
                    self.left_br = Node(node_value)
                else:
                    self.left_br.create_node(node_value)

        else:
            self.value = node_value


tree = Node(2)
print(vars(tree))

tree.create_node(3)
tree.create_node(5)
