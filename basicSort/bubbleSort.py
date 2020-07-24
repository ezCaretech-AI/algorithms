## 김결

def bubbleSort(a):
    n = len(a)-1
    for i in range(n, 0, -1):
        for j in range(1,i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]