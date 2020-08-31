import random

class node:
    def __init__(self, key=None):
        self.key = key
        
class binarySearch:
    def __init__(self):
        binarySearch.a = []
    
    def binarySearch(self, search_key):
        left = 0
        right = len(binarySearch.a) - 1
        
        while right >= left:
            mid = int((left+right) /2)
            
            if binarySearch.a[mid].key == search_key:
                return mid
            if binarySearch.a[mid].key > search_key:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1
    
    def insert(self, v):
        binarySearch.a.append(node(v))
    
    def run(self, key, searchValue):
        
        d = binarySearch()
        N = len(key)
        
        key = sorted(key)  ## 이진탐색은 정렬이 필요.
        
        for i in range(N):
            d.insert(key[i])
            
        for i in range(N):
            result = d.binarySearch(searchValue)
            if result == -1 or key[result] != searchValue:
                print('탐색오류')
