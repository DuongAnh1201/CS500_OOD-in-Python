def main():
    words = []
    #Task1: Get words from the user until "Exit"
    while True:
        word = input("Enter a word (or Exit to end): ")
        if word == "Exit":
            break

        words.append(word)

    print("The original list: ")
    print(words)
    sorted_words = sorted(words)
    print("The sorted list: ")
    print(sorted_words)
    print("The unique word: ")
    words.sort()
    pre = ""
    for word in words:
        if word != pre:
            print(word, end = ",")
        pre = word
    print("\n")
    
            


if __name__ == "__main__":
    main()
