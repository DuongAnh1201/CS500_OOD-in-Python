def expand(s:str, l:int, r:int):
    N = len(s)
    while (l>=0 and r<N) and s[l] == s[r]:
        l-=1
        r+=1
    return l, r
def palindrome(s: str) -> bool:
    best_L = 0
    best_R = 0
    N = len(s)
    if N == 0: return ""
    for i in range(N):
        l, r = expand(s, i, i)
        length = r-l-1
        if length>best_R-best_L+1:
            best_L = l+1
            best_R = r-1
        l, r = expand(s, i, i+1)
        length = r-l-1
        if length>best_R-best_L+1:
            best_L = l+1
            best_R = r-1
    return best_L, best_R

def main():
    s = input("Type in a sentence: ")
    best_L, best_R = palindrome(s)
    print(s[best_L:best_R+1])

if __name__ =="__main__":
    main()