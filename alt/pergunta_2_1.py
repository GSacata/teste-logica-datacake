# Pergunta 2.1: código alternativo da Pergunta 2
# Criada para treinar e exercitar árvore binária


class Node:
    def __init__(self, node_value):
        self.node_value = node_value
        self.node_l_br = None
        self.node_r_br = None


    def create_node(self, node_tree, node_num):
        node_num = int(node_num)

        if node_tree is None:
            node_tree = self.__init__(self, node_num)
        else:
            print("Foi pra outro node")
            pass

root_node = Node(3)
print(f"root_node: {vars(root_node)}")

root_node.create_node(root_node, 5)