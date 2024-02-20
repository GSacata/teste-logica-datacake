# Pergunta 2.1: código alternativo da Pergunta 2
# Criada para treinar e exercitar árvore binária

search_track = []

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

    def search_number(self, srch_number):
        
        if tree is None:
            print("No tree to search")
        
        elif srch_number == self.value:
            search_track.append(self.value)

        elif srch_number > self.value:
            search_track.append(self.value)
            self.right_br.search_number(srch_number)
        
        elif srch_number < self.value:
            search_track.append(self.value)
            self.left_br.search_number(srch_number)
        


tree = Node(2)

tree.create_node(3)
tree.create_node(5)
tree.create_node(4)
tree.create_node(7)

tree.search_number(3)
tree.search_number(4)

print(search_track)