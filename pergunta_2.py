class New_Tree():
    def __init__(self, value):
        self.value = value
        self.l_br = None
        self.r_br = None
        self.l_flag = 1
        self.r_flag = 1
        print(vars(self))
    
    def create_branches(self, value_l, value_r):
        self.l_br = New_Tree(value_l)
        self.r_br = New_Tree(value_r)
    
    def create_standard_tree(self):
        self.create_branches("Morango", "Pera")
        self.l_br.create_branches("Goiaba", "Limão")
        self.r_br.create_branches("", "Abacaxi")
        self.r_br.r_br.create_branches("", "Laranja")
        self.r_br.r_br.r_br.create_branches("Banana", "Cebola")

new_tree = New_Tree("Maçã")
new_tree.create_standard_tree()
# print(vars(new_tree.l_br.l_br))
# print(vars(new_tree.r_br.l_br))
# print(vars(new_tree.r_br.r_br.r_br))
# print(vars(new_tree.r_br.r_br.r_br.l_br))