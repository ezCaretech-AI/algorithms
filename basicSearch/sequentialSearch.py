import random

class node:
    def __init__(self, key=None):
        self.key = key

class sequentialSearch:
    def __init__(self):
        sequentialSearch.a = []
    
    def sequentialSearch(self, search_key):
        i = 0
        n = len(sequentialSearch.a)
                
        while i < n and sequentialSearch.a[i].key != search_key:
            i = i + 1
        
        if i == n:
            return -1
        else:
            return i
    
    def insert(self, v):
        sequentialSearch.a.append(node(v))
        
    def run(self, key, searchValue):
        
        d = sequentialSearch()
        N = len(key)
#         s_key = random.sample(range(0, N), N)
                
        for i in range(N):
            d.insert(key[i])
            
        for i in range(N):
            result = d.sequentialSearch(searchValue)
            if result == -1 or key[result] != searchValue:
                print('탐색오류')