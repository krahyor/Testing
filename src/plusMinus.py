def plusMinus(arr):
    positive = 0
    negative = 0
    zeros = 0
    for i in range(len(arr)):
        if arr[i] > 0 :
            positive+=1
        elif arr[i] < 0 :
            negative+=1
        else:
            zeros+=1
    return positive ,negative,zeros
