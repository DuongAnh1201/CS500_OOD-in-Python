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
    for i in range(len(words)):
        f = False
        for j in range(i):
            if words[i] == words[j]:
                f = True
                break
        if f == True:
            continue
        if i == 0:
            print(words[i], end = "")
        else:
            print(f", {words[i]}", end = "")
    print("\n")
        
    
            


if __name__ == "__main__":
    main()
