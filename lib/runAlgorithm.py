from lib import checkSort
import random, time

## 1. 정렬알고리즘
def runAlgorithmSort(funcs, funcsName, sampledata):
    n = len(sampledata)
    start_time=time.time()
    funcs(sampledata) # return 없이 sampledata가 바뀜
    end_time=time.time() - start_time
    
    print('%s 실행 시간 (N=%d) : %0.3f'%(funcsName, n, end_time))
    checkSort.checkSort(sampledata)
    print("")

## 2. 탐색알고리즘
def runAlgorithmSearch(funcs, funcsName, sampledata, test):
    n = len(sampledata)
    start_time=time.time()
    funcs(sampledata, test) # return 없이 sampledata가 바뀜
    end_time=time.time() - start_time

    print('%s 실행 시간 (N=%d) : %0.3f'%(funcsName, n, end_time))
    print("")