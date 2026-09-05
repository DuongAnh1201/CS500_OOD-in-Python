def valid(s: str)-> bool:
    '''
    This function will check if the input contains exactly 5 characters
    '''
    n = len(s)
    return n == 5

def check_case(s: str) -> tuple:
    '''
    The function will check if the string follow the pattern, or can change one word to follow the pattern or can not follow the pattern
    '''
    i = 0
    j = 4
    error = []
    while i<j:
        if s[i]!=s[j]:
            error.append((i,j))
        i+=1
        j-=1
    n = len(error)
    if n == 0:
        return True
    if n == 1:
        return (error[0])
    return False

def main():
    character_string = input("Enter a five-character string: ")
    if valid(character_string):
        result = check_case(character_string)
        if result == False:
            print(f"{character_string} does not follow the required pattern.")
            print("No single character replacement can make it follow the pattern.")
        elif result == True:
            print(f"{character_string} follows the required pattern.")
        else:
            print(f"{character_string} does not follow the required pattern.")
            new_string = ""
            for i in range(5):
                if i == result[1]:
                    new_string += character_string[result[0]]
                else:
                    new_string += character_string[i]
            print(f"Replace character {result[1]+1} with {character_string[result[0]]} to make it become {new_string}")
    else:
        print("Error: Invalid input: Please enter a five-character string.")
if __name__ == "__main__":
    main()