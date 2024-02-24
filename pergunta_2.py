tree_path = []
found_in_tree = 0
vars_cleared = True

class New_Tree():
    
    def __init__(self, value):
        self.value = value
        self.l_br = None
        self.r_br = None
        self.l_flag = 1
        self.r_flag = 1
    
    def create_branches(self, value_l, value_r):
        self.l_br = New_Tree(value_l)
        self.r_br = New_Tree(value_r)
    
    def create_standard_tree(self):
        self.create_branches("Morango", "Pera")
        self.l_br.create_branches("Goiaba", "Limão")
        self.r_br.create_branches("", "Abacaxi")
        self.r_br.r_br.create_branches("", "Laranja")
        self.r_br.r_br.r_br.create_branches("Banana", "Cebola")
    
    def write_tree_path(self, node_value):
        if tree_path.count(node_value) == 0:
            tree_path.append(node_value)
        elif tree_path.count(node_value) == 1:
            if self.l_flag == 0 and self.r_flag == 0:
                tree_path.remove(node_value)
            else:
                pass
        elif tree_path.count(node_value) >= 2:
            tree_path.remove(node_value)
    

    def search_tree(self, search_term):
        global tree_path, found_in_tree, vars_cleared
            

        print(f"Searching for '{search_term}' in {self.value}...")

        while found_in_tree == 0:
            self.write_tree_path(self.value)

            if self.value == search_term:
                found_in_tree += 1
                print(f"Found '{search_term}' at the following tree path:\n{tree_path}")
                vars_cleared = False
            
            else:

                if self.l_flag == 1 and found_in_tree == 0:
                    if self.l_br is None or self.value == '':
                        self.l_flag -= 1
                        continue
                    else:
                        self.l_flag -= 1
                        self.l_br.search_tree(search_term)
                
                if self.r_flag == 1 and found_in_tree == 0: # Aqui if não pode ser trocado por elif, pois com if, ao voltar do break, ele buscará no r_br do node anterior a este
                    if self.r_br is None or self.value == '':
                        self.r_flag -= 1
                        continue
                    else:
                        self.r_flag -= 1
                        self.r_br.search_tree(search_term)
                        self.write_tree_path(self.value)

                else:
                    pass # tanto galhos direito quanto esquerdo já foram buscados e não possuem valores
                    # por obséquio, não usar continue aqui
            
            break


new_tree = New_Tree("Maçã")
new_tree.create_standard_tree()

search_term = input("What word to find? ")
new_tree.search_tree(search_term)


print("code ended")

# planned update: criar um método que permite escrever a árvore (ex.: escreva o valor desse node, do galho esquerdo e do galho direito. Qual galho você quer ir? Escreva o valor blablabla...).
# planned update: o programa não para na primeira rota em que encontra o termo, ele continua rodando e entrega todas as rotas existentes com o termo buscado