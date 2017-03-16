def getRow(rowIndex):
    lists=[]
    if rowIndex<0:
        return lists
    for i in range(rowIndex+1):
        lists.append(1)
        for j in range(1,len(lists)):
            lists.insert(j,lists[j]+lists[j+1]

    print lists


    
