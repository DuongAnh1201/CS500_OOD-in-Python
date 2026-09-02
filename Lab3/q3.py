def merge(l1, l2):
    i = 0 
    j = 0
    result = []
    while i<len(l1) and j<len(l2):
        if l1[i]<=l2[j]:
            result.append(l1[i])
            i+=1
        else:
            result.append(l2[j])
            j+=1
    if i == len(l1):
        for k in range(j, len(l2)):
            result.append(l2[k])
    else:
        for k in range(i, len(l1)):
            result.append(l1[k])

    return result

def main():
    List1 = [1, 3, 5, 7]
    List2 = [2, 4, 6, 8]
    print(merge(List1, List2))

if __name__ == "__main__":
    main()