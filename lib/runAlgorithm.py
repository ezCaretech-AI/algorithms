from lib import checkSort
import random, time

def runAlgorithm(funcs, funcsName, sampledata):
    n = len(sampledata)
    start_time=time.time()
    funcs(sampledata)
    end_time=time.time() - start_time

    print('%s 실행 시간 (N=%d) : %0.3f'%(funcsName, n, end_time))
    checkSort.checkSort(sampledata)
    print("")