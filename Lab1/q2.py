from re import S


def is_palindrome(s: str)->bool:
    l = 0
    r = len(s)-1
    while l<=r:
        if s[l] == s[r]:
            l +=1
            r-=1
        else:
            return False
    return True

def main():
    s = input("Type in a string: ")
    print(is_palindrome(s))

if __name__ == "__main__":
    main()
        