
class tree_node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

class binarySearchTree:

    z = tree_node(key=0, left=0, right=0)
    z.left = z
    z.right = z
    head = tree_node(key=0, left=0, right=z)
    
    def binarySearchTree_search(self, search_key):
        x = self.head.right
        while x != self.z:
            if x.key == search_key:
                return x.key
            if x.key > search_key:
                x = x.left
            else:
                x = x.right
        return -1
    
    def binarySearchTree_insert(self, v):
        x = p = self.head
        while x != self.z:
            p = x
            if x.key == v:
                return
            if x.key > v:
                x = x.left
            else:
                x = x.right
        
        x = tree_node(key=v, left=self.z, right=self.z)
        if p.key > v:
            p.left = x
        else:
            p.right = x
    
    def run(self, key, searchValue):
        
        d = binarySearchTree()
        N = len(key)
        
        for i in range(N):
            d.binarySearchTree_insert(key[i])
        
        for i in range(N):
            result = d.binarySearchTree_search(searchValue)
            if result == -1 or result != searchValue:
                print('탐색오류')
        