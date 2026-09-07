def merge(l1, l2):
    ind_1 = 0 
    ind_2 = 0
    result = []
    while ind_1<len(l1) and ind_2<len(l2):
        if l1[ind_1]<=l2[ind_2]:
            result.append(l1[ind_1])
            ind_1+=1
        else:
            result.append(l2[ind_2])
            ind_2+=1
    if ind_1 == len(l1):
        for k in range(ind_2, len(l2)):
            result.append(l2[k])
    else:
        for k in range(ind_1, len(l1)):
            result.append(l1[k])

    return result

def main():
    List1 = [1, 3, 5, 7]
    List2 = [2, 4, 6, 8]
    print(merge(List1, List2))

if __name__ == "__main__":
    main()