class hashing:
    def __init__(self):
        hashing.a = [-1] * 10000
    
    def search(self, v):
        x = self.hash(v)
        while hashing.a[x] != -1:
            if v == hashing.a[x]:
                return hashing.a[x]
            else:
                x = (x + 1) % 10000
        return -1
    
    def insert(self, v):
        x = self.hash(v)
        while hashing.a[x] != -1:
            x = (x + 1) % 10000
        hashing.a[x] = v
    
    def hash(self, v):
        return v % 10000
    
    def print(self):
        for i in range(10000):
            if hashing.a[i] != -1:
                print('#', end='')
            else:
                print(' ', end='')
            if (i + 1) % 60 == 0:
                print()
    
    def run(self, key, searchValue):
        
        d = hashing()
        
        for i in range(len(key)):
            d.insert(key[i])
        
        for i in range(len(key)):
            result = d.search(searchValue)
            if result == -1 or result != searchValue:
                print('탐색오류')