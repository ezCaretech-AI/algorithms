def checkSort(a):
    isSorted=True
    for i in range(1, len(a)):
        if (a[i-1] > a[i]):
            isSorted = False
        if (not isSorted):
            break
    if isSorted:
        print("정렬 완료")
    else:
        print("정렬 실패")