def hanoi(peg, disk, storearray):
    if peg == 3:
        return 2 ** disk - 1

    if disk == 1:
        return 1

    if storearray[peg][disk] != 0:
        return storearray[peg][disk]

    min = 0
    n = disk
    k = disk - 1
    while k > 0:
        count = 2 * hanoi(peg, k, array) + hanoi(peg - 1, n - k, array)
        if min != 0:
            if min > count:
                min = count
        else:
            min = count
        k -= 1
    storearray[peg][disk] = min
    return min


array = [[0 for col in range(1024)] for row in range(1024)]

pegcount = int(input("기둥 개수:"))
diskcount = int(input("원판 개수:"))

print(hanoi(pegcount, diskcount, storearray=array))
