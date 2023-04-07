def count_str(listy):
    if len(listy)==1:
        if type(listy[0])==str:
            return 1
        else:
            return 0
    else:
        numby = count_str(listy[:len(listy)-1])
        if numby%1==numby:
            numby == [numby]
        if type(numby[0]) == str:
            numby+=1
        return numby



def count_str(listy):
    if listy ==[]:
        return 0
    else:
        if type(listy[0]) == str:
            return 1 + count_str(listy[1:])
        else:
            return count_str(listy[1:])
