def insertionSort(input_array):
    array_length = len(input_array)
    for i in range(1, array_length):
        val, idx=input_array[i],i
        while input_array[idx-1]>val and idx>0:
            input_array[idx]=input_array[idx-1]
            idx-=1
        input_array[idx]=val





