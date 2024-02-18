# Pergunta 2.1: código alternativo da Pergunta 2
# Criada para treinar e exercitar árvore binária


node_tree = None
root_node = None
# new_node_num = input("create int number node: ") # PROD-UNCOM
new_node_num = 3 # DEV-ER

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
    
    global root_node

    if root_node is None:
        root_node = created_node
    else:
        print("appended in another node")

def erase_created_node():
    global created_node
    created_node = None
    
created_node = create_node(new_node_num)
print(vars(created_node))

append_node()
erase_created_node()

print(created_node)
print(f"root_node: {vars(root_node)}")