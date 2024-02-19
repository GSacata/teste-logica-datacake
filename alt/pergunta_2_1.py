# Pergunta 2.1: código alternativo da Pergunta 2
# Criada para treinar e exercitar árvore binária


# class Node:
#     def __init__(self, node_value):
#         self.node_value = node_value
#         self.node_l_br = None
#         self.node_r_br = None


#     def create_node(self, node_tree, node_num):
#         node_num = int(node_num)

#         if node_tree is None:
#             # node_tree = self.__init__(self, node_num)
#             node_tree = self.__init__(node_num)
#         else:
#             print("Vai para outro node")

#             if node_num > self.node_value:
#                 print("vai para a direita") #DEV-ER
#                 # self.node_r_br = self.__init__(node_num)
#                 self.node_r_br = self.__init__(self, node_tree, node_num)
#             else:
#                 print("vai para a esquerda") #DEV-ER
#                 # self.node_l_br = self.__init__(node_num)
#                 self.node_l_br = self.__init__(self, node_tree, node_num)
            

# root_node = Node(3)
# print(f"root_node: {vars(root_node)}")

# root_node.create_node(root_node, 5)
# root_node.create_node(root_node, 2)

# print(f"root_node: {vars(root_node)}")


class Node():
    def __init__(self):
        return None
    
    def fill_node(self, node_obj, node_value):
        if 0 == 1:
            pass
        else:
            node_obj.value = node_value
            node_obj.left_br = {}
            node_obj.right_br = {}

tree = Node()
print(vars(tree))

tree.fill_node(tree, 3)
print(vars(tree))