class BST:
    def __init__(self, node, left = None, right = None):
        self.node = node
        self.left = left
        self.right = right
    
    def insert(self, new_node):

        if self.node == new_node:
            return

        elif self.node < new_node:
             if self.right == None:
                self.right = BST(new_node)

             else:
                self.right.insert(new_node)

        else:
             if self.left == None:
                self.left = BST(new_node)

             else:
                self.left.insert(new_node)


    def search(self, find_node):

        if self.node == find_node:
            return True
        
        elif self.node < find_node:
            if self.right == None:    
                return False

            else:
                self.right.search(find_node)

        else:
            if self.left == None:
                return False
            
            else:
                self.left.search(find_node)


## 올바른 코드
def search(self, find_node):

        if self.node == find_node:
            return True
        
        elif self.node < find_node and self.right != None:
            return self.right.search(find_node)

        elif self.node > find_node and self.left != None:
            return self.left.search(find_node)

        else:
            return False





my_BST = BST(50)
my_BST.insert(30)
my_BST.insert(70)
my_BST.insert(20)
my_BST.insert(40)

print(my_BST.search(70))
print(my_BST.search(60)
my_BST.search(40)





