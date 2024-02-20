tree = {
    "value": "Maçã",
    "left_br": {
        "value": "Morango", 
        "left_br": {
            "value": "Goiaba", 
            "left_br": {},
            "right_br": {}
        },
        "right_br": {
            "value": "Limão", 
            "left_br": {},
            "right_br": {}
        }
    },
    "right_br": {
        "value": "Pera", 
        "left_br": {},
        "right_br": {
            "value": "Abacaxi", 
            "left_br": {},
            "right_br": {
                "value": "Laranja", 
                "left_br": {
                    "value": "Banana", 
                    "left_br": {},
                    "right_br": {}
                },
                "right_br": {
                    "value": "Cebola", 
                    "left_br": {},
                    "right_br": {}
                }
            }
        }
    }
}

text_input = input("What word to find? ")

def format_input():
    print("Formatting the input...")

def search_tree():
    print("Searching the tree...")


test_obj = {
    "value": "", 
    "l_br": {},
    "l_flag": 1,
    "r_br": {},
    "r_flag": 1
    }

class Tree():
    def __init__(self, tree):
        self.tree = tree
    
    def hello_tree(self):
        print("Hello to the trees of the world")

new_tree = Tree(tree)

print(vars(new_tree))
new_tree.hello_tree()