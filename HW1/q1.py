from ast import List


def is_prime(upper_limit: int) -> List:
    '''
    The function using Eratosthenes
    '''
    prime = [True]*(upper_limit+1)
    prime[0] = prime[1] = False
    for i in range(2, upper_limit+1):
        if prime[i] == True:
            for j in range(i*2, upper_limit, i):
                prime[j] = False
    return prime
    
def main():
    upper_bound = int(input("Enter the upper limit: "))
    prime = is_prime(upper_bound)
    if upper_bound<2:
        print(f"There is no sexy prime pair in the range of upper bound equal to {upper_bound}")
        return
    result = []
    for i in range(2, upper_bound+1):
        if prime[i] == True and i+6<= upper_bound and prime[i+6] == True:
            result.append((i, i+6))
    if len(result) == 0:
        print(f"There is no sexy prime pair in the range of upper bound equal to {upper_bound}")
        return
    for pair in result:
        print(pair)
    


if __name__ == "__main__":
    main()
