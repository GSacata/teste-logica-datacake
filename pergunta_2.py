path = []

class New_Tree():
    
    def __init__(self, value):
        self.value = value
        self.l_br = None
        self.r_br = None
        self.l_flag = 1
        self.r_flag = 1
        self.found = 0
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
    
    def search_tree(self, search_term):
        global path

        print(f"Searching for '{search_term}' in {self.value}...")

        while self.found == 0:

            if self.value == search_term:
                self.found += 1
                print(f"Found '{search_term}' at the following path:\n{path}")
            
            else:

                if self.l_flag == 1:
                    if self.l_br is None or self.value == '':
                        self.l_flag -= 1
                        continue
                    else:
                        self.l_br.search_tree(search_term)
                
                if self.r_flag == 1:
                    if self.r_br is None or self.value == '':
                        self.r_flag -= 1
                        continue
                    else:
                        self.r_br.search_tree(search_term)
                
                else:
                    pass # tanto galhos direito quanto esquerdo já foram buscados e não possuem valores
                    # por obséquio, não usar continue aqui
            
            break



new_tree = New_Tree("Maçã")
new_tree.create_standard_tree()

new_tree.search_tree("Cebola")

print("code ended")

# Mais para frente: criar um método que permite escrever a árvore (ex.: escreva o valor desse node, do galho esquerdo e do galho direito. Qual galho você quer ir? Escreva o valor blablabla...).