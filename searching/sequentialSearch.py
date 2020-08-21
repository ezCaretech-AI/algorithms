import random

class node:
    def __init__(self, key=None):
        self.key = key

class SequentialSearch:
    def __init__(self):
        SequentialSearch.a = []
    
    def sequentialSearch(self, search_key):
        i = 0
        n = len(SequentialSearch.a)
                
        while i < n and SequentialSearch.a[i].key != search_key:
            i = i + 1
        
        if i == n:
            return -1
        else:
            return i
    
    def insert(self, v):
        SequentialSearch.a.append(node(v))
        
    def run(self, key, searchValue):
        
        d = SequentialSearch()
        N = len(key)
#         s_key = random.sample(range(0, N), N)
                
        for i in range(N):
            d.insert(key[i])
            
        for i in range(N):
            result = d.sequentialSearch(searchValue)
            if result == -1 or key[result] != searchValue:
                print('탐색오류')